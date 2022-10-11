from django.apps import AppConfig


class NewsprojConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsproj'

    def ready(self):
        import newsproj.signals