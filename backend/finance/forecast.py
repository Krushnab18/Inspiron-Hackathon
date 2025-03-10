import pandas as pd
from prophet import Prophet
from .models import FinancialData, UserProfile, ForecastData
from django.http import JsonResponse



def generate_forecasts(user_email):
    """
    Generate sales, COGS, and profit forecasts for a user and store the data in the database.
    """
    try:
        # Step 1: Retrieve data from the database
        user = UserProfile.objects.get(email=user_email)
        financial_data = FinancialData.objects.filter(user=user).values('date', 'sales', 'cogs', 'profit')
        df = pd.DataFrame(list(financial_data))
        df['date'] = pd.to_datetime(df['date'])
        # key_metrics = calculate_key_metrics(df)

        # Step 2: Prepare data for Prophet
        sales_df = df[['date', 'sales']].rename(columns={'date': 'ds', 'sales': 'y'})
        cogs_df = df[['date', 'cogs']].rename(columns={'date': 'ds', 'cogs': 'y'})
        profit_df = df[['date', 'profit']].rename(columns={'date': 'ds', 'profit': 'y'})

        # Step 3: Train Prophet models
        sales_model = Prophet()
        sales_model.fit(sales_df)

        cogs_model = Prophet()
        cogs_model.fit(cogs_df)

        profit_model = Prophet()
        profit_model.fit(profit_df)

        # Step 4: Make forecasts
        future = sales_model.make_future_dataframe(periods=365)
        sales_forecast = sales_model.predict(future)
        cogs_forecast = cogs_model.predict(future)
        profit_forecast = profit_model.predict(future)

        # Step 5: Store forecasts in the database
        for date, sales, cogs, profit in zip(future['ds'], sales_forecast['yhat'], cogs_forecast['yhat'], profit_forecast['yhat']):
            ForecastData.objects.update_or_create(
                user=user,
                date=date,
                defaults={
                    'sales_forecast': sales,
                    'cogs_forecast': cogs,
                    'profit_forecast': profit
                }
            )

        print("Forecast data successfully stored in the database.")

    except Exception as e:
        print(f"Error generating forecasts: {e}")
        return None