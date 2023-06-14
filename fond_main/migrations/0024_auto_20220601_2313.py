# Generated by Django 3.2.5 on 2022-06-01 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fond_main', '0023_auto_20220502_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='technician1_failed',
            field=models.ForeignKey(blank=True, db_column='technician1_failed', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_technician1_failed', to='fond_main.staff'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='technician2_failed',
            field=models.ForeignKey(blank=True, db_column='technician2_failed', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_technician2_failed', to='fond_main.staff'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='technician3_failed',
            field=models.ForeignKey(blank=True, db_column='technician3_failed', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_technician3_failed', to='fond_main.staff'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='difficaulty',
            field=models.FloatField(blank=True, choices=[(1, 1), (1.25, 1.25), (1.5, 1.5)], default=1.0, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='mistake_part',
            field=models.CharField(blank=True, choices=[('Operational Part', 'Operational Part'), ('Config Part', 'Config Part'), ('Operational/Config Part', 'Operational/Config Part'), ('Technical Part', 'Technical Part'), ('Technician Part', 'Technician Part'), ('Technical/Technician Part', 'Technical/Technician Part'), ('Technical/Technician/Config Part', 'Technical/Technician/Config Part'), ('Technical/Technician/Operational Part', 'Technical/Technician/OP Part')], default='', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('Measuring', 'Measuring'), ('Servicing', 'Servicing'), ('Construction', 'Construction'), ('Welding', 'Welding'), ('Design', 'Design'), ('Connection', 'Connection'), ('Emergency', 'Emergency')], default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='trubka',
            field=models.IntegerField(blank=True, choices=[(-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
    ]