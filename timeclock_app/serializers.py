from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Punch, DailyHours, WeeklyHours

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

# Punch Serializer
class PunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punch
        fields = ['id', 'user', 'punch_type', 'timestamp']
        
# DailyHours Serializer
class DailyHoursSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display username instead of ID

    class Meta:
        model = DailyHours
        fields = ['id', 'user', 'date', 'total_hours', 'regular_hours', 'overtime_hours']

# WeeklyHours Serializer
class WeeklyHoursSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display username instead of ID

    class Meta:
        model = WeeklyHours
        fields = ['id', 'user', 'week_start_date', 'week_end_date', 'total_hours', 'regular_hours', 'overtime_hours']
