# Generated by Django 4.0.2 on 2022-04-24 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_cvonline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='active',
        ),
        migrations.AddField(
            model_name='userlessonview',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
