# Generated by Django 3.2.5 on 2022-03-29 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fond_main', '0006_auto_20220329_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='performing_date',
            new_name='registration_date',
        ),
    ]
