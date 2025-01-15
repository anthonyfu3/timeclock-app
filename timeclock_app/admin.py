from django.contrib import admin
from .models import Profile, Punch, DailyHours, WeeklyHours

admin.site.register(Profile)
admin.site.register(Punch)
admin.site.register(DailyHours)
admin.site.register(WeeklyHours)
