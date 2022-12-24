from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register('plans/', views.PlanList.as_view())

urlpatterns = [
    path('plans/', views.PlanList.as_view()),
    path('plans/<int:id>/', views.PlanDetail.as_view()),
    path('tags/', views.TagList.as_view()),
    path('tags/<int:id>/', views.TagDetail.as_view())
]
