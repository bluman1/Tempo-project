# Generated by Django 2.0.7 on 2018-10-24 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_email',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='visitor',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
