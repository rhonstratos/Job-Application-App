from django.apps import AppConfig


class JobappConfig(AppConfig):
    name = 'jobapp'

    def ready(self):
        from . import models