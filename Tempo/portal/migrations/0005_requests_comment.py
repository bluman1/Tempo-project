# Generated by Django 2.0.7 on 2018-11-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_requests'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='comment',
            field=models.CharField(default='none', max_length=500),
            preserve_default=False,
        ),
    ]
