# Generated by Django 4.1.4 on 2023-01-16 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0006_alter_comments_date_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 16, 16, 39, 17, 983671)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 16, 16, 39, 17, 983671)),
        ),
    ]
