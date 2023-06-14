# Generated by Django 3.2.5 on 2022-04-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fond_main', '0019_auto_20220419_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='quality_status',
            field=models.CharField(choices=[('', ''), ('Checked', 'Checked'), ('Incomplete', 'Incomplete'), ('Corrected', 'Corrected'), ('Solved', 'Solved'), ('Punishment', 'Punishment')], default='', max_length=60),
        ),
    ]