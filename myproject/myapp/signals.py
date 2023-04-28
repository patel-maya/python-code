from django.db.models.signals import post_migrate,pre_migrate
from django.dispatch import receiver

from django.apps import apps

# @receiver(pre_migrate)
# def log_migration_applied(sender, **kwargs):
    # print("Migration applied to app:", sender.label)
    # a=(kwargs.get('apps'))
    # aa = a.get_state()
    # for ab in aa:
    #   print(ab.name)

# def my_function():
    # state = apps.get_model('myapp', 'Author')
    # print(f"Model name: {state.__name__}")
    # for model in state._meta.get_fields():
    #     field_name = model.name
    #     # field_type = model.get_internal_type()
    # print(f"Field name: {field_name}")

    # for migration, _ in kwargs.get('plan', []):
    #     # import pdb;pdb.set_trace()
    #     if migration=='myapp':
    #       migration_name = migration.name
    #       for operation in migration.operations:
    #         model_name = operation.model_name
    #         field_names = [f.name for f in operation.fields]
    #         print(f"  - {migration_name}: {model_name} ({', '.join(field_names)})")
from django.apps import apps
from django.db import migrations



def log_migration_applied(sender, **kwargs):
    plan = kwargs.get('plan')
    added_fields = set()
    removed_fields = set()
    for migration, backwards in plan:
        # print(backwards)
        for operation in migration.operations:
            app_label = migration.app_label
            if isinstance(operation, migrations.AddField):
                model_name = operation.model_name
                field_name = operation.name
                if field_name not in added_fields:
                    added_fields.add(field_name)
                    print(f"Field '{field_name}' has been added to model '{model_name}' in app '{app_label}'")
            elif isinstance(operation, migrations.RemoveField):
                model_name = operation.model_name
                field_name = operation.name
                if field_name not in removed_fields:
                    removed_fields.add(field_name)
                    print(f"Field '{field_name}' has been removed from model '{model_name}' in app '{app_label}'")
from django.db.models.signals import class_prepared
from django.dispatch import receiver

# @receiver(class_prepared)
# def log_new_model(sender, **kwargs):
#     model = sender
#     app_label = model._meta.app_label
#     model_name = model.__name__
#     if not model._meta.abstract:
#         # Check if the model is not abstract
#         print(f"New model '{model_name}' has been created in app '{app_label}'")
# from django.db.models.signals import pre_delete
# from django.dispatch import receiver

# @receiver(pre_delete)
# def log_deleted_model(sender, instance, **kwargs):
#     model = sender
#     app_label = model._meta.app_label
#     model_name = model.__name__
#     if not model.objects.exclude(pk=instance.pk).exists():
#         # If this is the last object of the model being deleted, print a message indicating that the model is being deleted
#         print(f"Model '{model_name}' in app '{app_label}' is being deleted")

