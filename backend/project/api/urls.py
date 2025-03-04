from django.urls import path
from finance.views import get_data, get_key_metrics, generate_insights_with_recommendations

urlpatterns = [
    path('get_data/<str:user_email>/<str:data_type>/', get_data, name='get_data'),
    path('get_key_metrics/<str:user_email>/', get_key_metrics, name='get_key_metrics'),
    path('generate_insights_with_recommendations/<str:user_email>/', generate_insights_with_recommendations, name='generate_insights_with_recommendations'),
]