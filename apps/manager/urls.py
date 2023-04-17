from django.urls import path

from apps.manager.views import get_all_operation, get_all_incomes, get_all_consumptions

urlpatterns = [
    path("operations", get_all_operation, name="get_all_operations"),
    path("operations/incomes", get_all_incomes, name="get_all_incomes"),
    path("operations/consumptions", get_all_consumptions, name="get_all_consumptions"),
]
