# Generated by Django 4.2 on 2023-04-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]