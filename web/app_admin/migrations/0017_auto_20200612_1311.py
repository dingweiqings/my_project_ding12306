# Generated by Django 3.0.5 on 2020-06-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0016_auto_20200607_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='waituser',
            name='reason',
            field=models.CharField(default='SUCCESS', max_length=50),
        ),
        migrations.AddField(
            model_name='waituser',
            name='result',
            field=models.BooleanField(default=True),
        ),
    ]
