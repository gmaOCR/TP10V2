# Generated by Django 3.2.5 on 2023-03-24 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
