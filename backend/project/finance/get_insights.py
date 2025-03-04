from django.db.models import Sum, Avg
from datetime import timedelta
from django.utils.timezone import now
from .models import FinancialData
from user.models import UserProfile

def get_user_data(email):
    """Fetch user profile by email."""
    try:
        return UserProfile.objects.get(email=email)
    except UserProfile.DoesNotExist:
        return None

def get_top_performing_products(email):
    """Identify top-performing products for a specific user based on total sales."""
    user = get_user_data(email)
    if not user:
        return {"error": "User not found"}

    top_products = (
        FinancialData.objects.filter(user=user)
        .values("product")
        .annotate(total_sales=Sum("sales"))
        .order_by("-total_sales")[:5]
    )
    return [{"product": p["product"], "total_sales": p["total_sales"]} for p in top_products]

def get_underperforming_products(email):
    """Identify underperforming products for a specific user."""
    user = get_user_data(email)
    if not user:
        return {"error": "User not found"}

    low_products = (
        FinancialData.objects.filter(user=user)
        .values("product")
        .annotate(total_sales=Sum("sales"))
        .order_by("total_sales")[:5]
    )
    return [{"product": p["product"], "total_sales": p["total_sales"]} for p in low_products]

def get_region_based_demand_shifts(email):
    """Analyze region-based demand changes over time for a specific user."""
    user = get_user_data(email)
    if not user:
        return {"error": "User not found"}

    recent_date = FinancialData.objects.filter(user=user).latest("date").date
    past_date = recent_date - timedelta(days=30)

    recent_sales = (
        FinancialData.objects.filter(user=user, date__gte=past_date)
        .values("country", "product")
        .annotate(total_sales=Sum("sales"))
    )

    past_sales = (
        FinancialData.objects.filter(user=user, date__lt=past_date, date__gte=past_date - timedelta(days=30))
        .values("country", "product")
        .annotate(total_sales=Sum("sales"))
    )

    demand_shifts = []
    for rec in recent_sales:
        past_rec = next((p for p in past_sales if p["product"] == rec["product"] and p["country"] == rec["country"]), None)
        if past_rec:
            change = rec["total_sales"] - past_rec["total_sales"]
            if abs(change) > 0.1 * past_rec["total_sales"]:
                demand_shifts.append({
                    "product": rec["product"],
                    "country": rec["country"],
                    "sales_change": change,
                    "trend": "Increase" if change > 0 else "Decrease"
                })

    return demand_shifts

def get_high_return_or_low_profit_products(email):
    """Identify products with high return rates or low profits for a specific user."""
    user = get_user_data(email)
    if not user:
        return {"error": "User not found"}

    problem_products = (
        FinancialData.objects.filter(user=user)
        .values("product")
        .annotate(
            average_profit=Avg("profit"),
            return_rate=Avg("cogs") / Avg("sales")
        )
        .filter(average_profit__lt=0.1 * Avg("sales"))
    )

    return [{"product": p["product"], "profit_margin": p["average_profit"], "return_rate": p["return_rate"]} for p in problem_products]

def detect_sales_spikes_or_drops(email):
    """Detect sales spikes or drops for a specific user."""
    user = get_user_data(email)
    if not user:
        return {"error": "User not found"}

    recent_date = FinancialData.objects.filter(user=user).latest("date").date
    past_date = recent_date - timedelta(days=30)

    recent_sales = (
        FinancialData.objects.filter(user=user, date__gte=past_date)
        .values("product")
        .annotate(total_sales=Sum("sales"))
    )

    past_sales = (
        FinancialData.objects.filter(user=user, date__lt=past_date, date__gte=past_date - timedelta(days=30))
        .values("product")
        .annotate(total_sales=Sum("sales"))
    )

    spikes_drops = []
    for rec in recent_sales:
        past_rec = next((p for p in past_sales if p["product"] == rec["product"]), None)
        if past_rec:
            change = rec["total_sales"] - past_rec["total_sales"]
            if abs(change) > 0.2 * past_rec["total_sales"]:
                spikes_drops.append({
                    "product": rec["product"],
                    "sales_change": change,
                    "trend": "Spike" if change > 0 else "Drop"
                })

    return spikes_drops