from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register('plans/', views.PlanList.as_view())

urlpatterns = [
    path('plans/', views.PlanList.as_view())
]
