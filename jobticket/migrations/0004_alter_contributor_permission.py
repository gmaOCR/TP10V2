# Generated by Django 3.2.5 on 2023-03-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobticket', '0003_auto_20230326_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='permission',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='permission'),
        ),
    ]
