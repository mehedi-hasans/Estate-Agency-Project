from django.apps import AppConfig
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

class IndexConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'index'
