# Generated by Django 3.2.5 on 2022-04-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fond_main', '0020_alter_ticket_quality_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='quality_status',
            field=models.CharField(blank=True, choices=[('', ''), ('Checked', 'Checked'), ('Incomplete', 'Incomplete'), ('Corrected', 'Corrected'), ('Solved', 'Solved'), ('Punishment', 'Punishment')], default='', max_length=60, null=True),
        ),
    ]