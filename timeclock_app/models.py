from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = (
        ('employee', 'Employee'),
        ('supervisor', 'Supervisor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Punch(models.Model):
    PUNCH_TYPE_CHOICES = (
        ('punch_in', 'Punch In'),
        ('punch_out', 'Punch Out'),
        ('lunch_in', 'Lunch In'),
        ('lunch_out', 'Lunch Out'),
        ('ot_in', 'OT In'),
        ('ot_out', 'OT Out'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="punches")
    punch_type = models.CharField(max_length=20, choices=PUNCH_TYPE_CHOICES)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.punch_type} at {self.timestamp}"


class DailyHours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="daily_hours")
    date = models.DateField()
    total_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    regular_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.user.username} - {self.date} Total: {self.total_hours}"



class WeeklyHours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="weekly_hours")
    week_start_date = models.DateField()
    week_end_date = models.DateField()
    total_hours = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    regular_hours = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    overtime_hours = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.user.username} - Week of {self.week_start_date}"

