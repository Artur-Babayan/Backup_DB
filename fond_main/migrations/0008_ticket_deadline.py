# Generated by Django 3.2.5 on 2022-03-29 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fond_main', '0007_rename_performing_date_ticket_registration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='deadline',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
    ]
