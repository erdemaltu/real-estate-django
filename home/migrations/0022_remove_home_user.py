# Generated by Django 3.2 on 2021-06-30 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_home_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='user',
        ),
    ]
