from django.apps import AppConfig

from core import agenda


class AgendaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.agenda'
