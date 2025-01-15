from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import UserViewSet, PunchViewSet, DailyHoursViewSet, WeeklyHoursViewSet, supervisor_dashboard

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'punches', PunchViewSet, basename='punch')
router.register(r'daily_hours', DailyHoursViewSet, basename='daily_hours')
router.register(r'weekly_hours', WeeklyHoursViewSet, basename='weekly_hours')


# Include the router's URLs
urlpatterns = [
    path('', include(router.urls)),
]
