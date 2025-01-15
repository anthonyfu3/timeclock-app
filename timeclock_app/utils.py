from datetime import timedelta
from .models import Punch, DailyHours, WeeklyHours

def calculate_daily_hours(user, date):
    # Function to calculate daily hours
    punches = Punch.objects.filter(user=user, timestamp__date=date).order_by('timestamp')
    total_seconds = 0
    punch_in_time = None

    for punch in punches:
        if punch.punch_type == 'punch_in':
            punch_in_time = punch.timestamp
        elif punch.punch_type == 'punch_out' and punch_in_time:
            total_seconds += (punch.timestamp - punch_in_time).total_seconds()
            punch_in_time = None

    total_hours = total_seconds / 3600
    regular_hours = min(total_hours, 8)
    overtime_hours = max(total_hours - 8, 0)

    daily_hours, created = DailyHours.objects.update_or_create(
        user=user,
        date=date,
        defaults={
            'total_hours': round(total_hours, 2),
            'regular_hours': round(regular_hours, 2),
            'overtime_hours': round(overtime_hours, 2),
        }
    )
    return daily_hours

def calculate_weekly_hours(user, week_start_date, week_end_date):
    # Function to calculate weekly hours
    daily_hours = DailyHours.objects.filter(
        user=user,
        date__gte=week_start_date,
        date__lte=week_end_date
    )

    total_hours = sum(dh.total_hours for dh in daily_hours)
    regular_hours = sum(dh.regular_hours for dh in daily_hours)
    overtime_hours = sum(dh.overtime_hours for dh in daily_hours)

    weekly_hours, created = WeeklyHours.objects.update_or_create(
        user=user,
        week_start_date=week_start_date,
        week_end_date=week_end_date,
        defaults={
            'total_hours': round(total_hours, 2),
            'regular_hours': round(regular_hours, 2),
            'overtime_hours': round(overtime_hours, 2),
        }
    )
    return weekly_hours
