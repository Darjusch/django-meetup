# Generated by Django 3.2.6 on 2021-08-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0006_remove_meetup_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-08-30'),
            preserve_default=False,
        ),
    ]
