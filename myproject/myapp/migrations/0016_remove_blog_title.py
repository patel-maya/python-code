# Generated by Django 4.2 on 2023-04-25 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
    ]
