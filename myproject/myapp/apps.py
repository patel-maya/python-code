from django.apps import AppConfig
# from django.conf import settings
from django.db.models.signals import pre_migrate
from . signals import *
 
class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        pre_migrate.connect(log_migration_applied, sender=self)

# from django.apps import AppConfig

# class MyAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'myapp'

#     def ready(self):
#         import myapp.signals
