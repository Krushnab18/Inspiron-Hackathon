from django.shortcuts import render
from finance.models import ForecastData, FinancialData
from user.models import UserProfile
from django.http import JsonResponse
from rest_framework.decorators import api_view
import pandas as pd
from .get_insights import (
    get_top_performing_products,
    get_underperforming_products,
    get_region_based_demand_shifts,
    get_high_return_or_low_profit_products,
    detect_sales_spikes_or_drops
)
from .llm_service import generate_recommendation

@api_view(['GET'])
def get_data(request, user_email, data_type):
    try:
        user = UserProfile.objects.get(email=user_email)

        if data_type == "historical":
            data = FinancialData.objects.filter(user=user).values('date', 'sales', 'cogs', 'profit')
        elif data_type == "forecast":
            data = ForecastData.objects.filter(user=user).values('date', 'sales_forecast', 'cogs_forecast', 'profit_forecast')
        else:
            return JsonResponse({'error': 'Invalid data type'}, status=400)

        # Transform data into the format expected by the frontend
        formatted_data = [
            {
                'date': f"new Date({entry['date'].year}, {entry['date'].month - 1}, {entry['date'].day})",
                'sales': entry.get('sales') or entry.get('sales_forecast'),
                'cogs': entry.get('cogs') or entry.get('cogs_forecast'),
                'profit': entry.get('profit') or entry.get('profit_forecast'),
            }
            for entry in data
        ]

        return JsonResponse(formatted_data, safe=False)

    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
def get_key_metrics(request, user_email):
    try:
        # Retrieve user and financial data
        user = UserProfile.objects.get(email=user_email)
        financial_data = FinancialData.objects.filter(user=user).values('date', 'sales', 'cogs', 'profit')
        df = pd.DataFrame(list(financial_data))

        if df.empty:
            return JsonResponse({"error": "No financial data found for this user"}, status=404)

        # Calculate key metrics
        total_revenue = df['sales'].sum()
        total_cogs = df['cogs'].sum()
        total_profit = df['profit'].sum()

        gross_profit_margin = ((total_revenue - total_cogs) / total_revenue) * 100 if total_revenue != 0 else 0
        net_profit_margin = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0
        cogs_percentage = (total_cogs / total_revenue) * 100 if total_revenue != 0 else 0

        key_metrics = {
            "total_revenue": total_revenue,
            "total_cogs": total_cogs,
            "total_profit": total_profit,
            "gross_profit_margin": round(gross_profit_margin, 2),
            "net_profit_margin": round(net_profit_margin, 2),
            "cogs_percentage": round(cogs_percentage, 2),
        }

        return JsonResponse(key_metrics)

    except UserProfile.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)



@api_view(['GET'])
def generate_insights_with_recommendations(request, user_email):
    insights = {
        "top_performing_products": get_top_performing_products(user_email),
        "underperforming_products": get_underperforming_products(user_email),
        "region_based_demand_shifts": get_region_based_demand_shifts(user_email),
        "high_return_or_low_profit_products": get_high_return_or_low_profit_products(user_email),
        "sales_spikes_or_drops": detect_sales_spikes_or_drops(user_email),
    }
    print(insights)
    recommendations = []

    for category, items in insights.items():
        for item in items:
            insight_text = f"{category.replace('_', ' ').title()}: {item}"
            recommendation = generate_recommendation(insight_text)
            recommendations.append({
                # "insight": insight_text,
                "recommendation": recommendation
            })

    return JsonResponse({"recommendations": recommendations})