# Generated by Django 4.2 on 2023-04-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='age2',
            field=models.IntegerField(null=True),
        ),
    ]