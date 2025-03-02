import json
import pandas as pd
from prophet import Prophet
from .models import FinancialData, UserProfile

def calculate_key_metrics(df):
    """
    Calculate key profitability metrics from the financial data.
    """
    total_revenue = df['sales'].sum()
    total_cogs = df['cogs'].sum()
    total_profit = df['profit'].sum()

    # Calculate metrics
    gross_profit_margin = ((total_revenue - total_cogs) / total_revenue) * 100 if total_revenue != 0 else 0
    net_profit_margin = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0
    cogs_percentage = (total_cogs / total_revenue) * 100 if total_revenue != 0 else 0

    # Return metrics as a dictionary
    return {
        "total_revenue": total_revenue,
        "total_cogs": total_cogs,
        "total_profit": total_profit,
        "gross_profit_margin": gross_profit_margin,
        "net_profit_margin": net_profit_margin,
        "cogs_percentage": cogs_percentage,
    }


def generate_forecasts(user_email):
    """
    Generate sales, COGS, and profit forecasts for a user and save the data as a .json file.
    """
    try:
        # Step 1: Retrieve data from the database
        user = UserProfile.objects.get(email=user_email)
        financial_data = FinancialData.objects.filter(user=user).values('date', 'sales', 'cogs', 'profit')
        df = pd.DataFrame(list(financial_data))
        df['date'] = pd.to_datetime(df['date'])
        key_metrics = calculate_key_metrics(df)
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

        # Step 5: Format data for Chart.js
        chart_data = {
            "labels": sales_forecast['ds'].dt.strftime('%Y-%m-%d').tolist(),
            "datasets": [
                {
                    "label": "Sales Forecast",
                    "data": sales_forecast['yhat'].tolist(),
                    "lowerBound": sales_forecast['yhat_lower'].tolist(),
                    "upperBound": sales_forecast['yhat_upper'].tolist(),
                    "borderColor": "rgba(75, 192, 192, 1)",
                    "backgroundColor": "rgba(75, 192, 192, 0.2)"
                },
                {
                    "label": "COGS Forecast",
                    "data": cogs_forecast['yhat'].tolist(),
                    "lowerBound": cogs_forecast['yhat_lower'].tolist(),
                    "upperBound": cogs_forecast['yhat_upper'].tolist(),
                    "borderColor": "rgba(255, 99, 132, 1)",
                    "backgroundColor": "rgba(255, 99, 132, 0.2)"
                },
                {
                    "label": "Profit Forecast",
                    "data": profit_forecast['yhat'].tolist(),
                    "lowerBound": profit_forecast['yhat_lower'].tolist(),
                    "upperBound": profit_forecast['yhat_upper'].tolist(),
                    "borderColor": "rgba(153, 102, 255, 1)",
                    "backgroundColor": "rgba(153, 102, 255, 0.2)"
                }
            ],
            "key_metrics": key_metrics  # Include key metrics in the JSON
        }

        # Step 6: Save the data as a .json file
        file_path = f'user/static/user/data/forecast_data_{user_email}.json'
        with open(file_path, 'w') as f:
            json.dump(chart_data, f, indent=4)

        print(f"Forecast data saved to {file_path}")
        # return file_path

    except Exception as e:
        print(f"Error generating forecasts: {e}")
        return None