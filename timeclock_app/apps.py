from django.apps import AppConfig # type: ignore

class TimeclockAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'timeclock_app'

    def ready(self):
        import timeclock_app.signals