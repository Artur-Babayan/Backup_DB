# Generated by Django 3.2.5 on 2022-03-31 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fond_main', '0009_alter_ticket_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='bcrm_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='rt_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketing_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]