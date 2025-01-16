from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .models import Punch, DailyHours, WeeklyHours
from .serializers import UserSerializer, PunchSerializer, DailyHoursSerializer, WeeklyHoursSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import render

# User API View
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # Only admin users can manage users

# Punch API View
class PunchViewSet(ModelViewSet):
    queryset = Punch.objects.all()
    serializer_class = PunchSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users can manage punches

# DailyHours API View
class DailyHoursViewSet(ModelViewSet):
    queryset = DailyHours.objects.all()
    serializer_class = DailyHoursSerializer
    permission_classes = [IsAuthenticated]

# WeeklyHours API View
class WeeklyHoursViewSet(ModelViewSet):
    queryset = WeeklyHours.objects.all()
    serializer_class = WeeklyHoursSerializer
    permission_classes = [IsAuthenticated]
    
def supervisor_dashboard(request):
    # Fetch latest punches
    latest_punches = Punch.objects.select_related('user').order_by('-timestamp')[:10]  # Show the 10 latest punches
    
    # Fetch daily and weekly hours
    daily_hours = DailyHours.objects.select_related('user').all()
    weekly_hours = WeeklyHours.objects.select_related('user').all()
    users = User.objects.all()
    return render(request, 'timeclock_app/supervisor_dashboard.html', { # type: ignore
        'latest_punches': latest_punches,
        'daily_hours': daily_hours,
        'weekly_hours': weekly_hours,
        'users': users,
    })