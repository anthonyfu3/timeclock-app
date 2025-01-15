from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from timeclock_app.views import supervisor_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timeclock/', include('timeclock_app.urls')),  # This now directly serves API routes
    path('admin_dashboard/', supervisor_dashboard, name='supervisor_dashboard'),  
    path('', lambda request: HttpResponseRedirect('/timeclock/')),  # Redirect root to /timeclock/
]
