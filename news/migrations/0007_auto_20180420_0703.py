# Generated by Django 2.0.4 on 2018-04-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20180420_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='Посилання'),
        ),
    ]
