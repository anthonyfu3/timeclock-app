from django.db.models.signals import post_save # type: ignore
from django.dispatch import receiver # type: ignore
from .models import Punch
from .utils import calculate_daily_hours, calculate_weekly_hours
from datetime import timedelta

@receiver(post_save, sender=Punch)
def update_hours(sender, instance, **kwargs):
    # Calculate daily hours
    calculate_daily_hours(instance.user, instance.timestamp.date())

    # Calculate weekly hours
    week_start_date = instance.timestamp.date() - timedelta(days=instance.timestamp.date().weekday())
    week_end_date = week_start_date + timedelta(days=6)
    calculate_weekly_hours(instance.user, week_start_date, week_end_date)
