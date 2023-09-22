# Generated by Django 4.2.5 on 2023-09-22 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_feedback_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.date(2023, 9, 22)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='media',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
