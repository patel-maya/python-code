# Generated by Django 4.2 on 2023-04-24 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
    ]
