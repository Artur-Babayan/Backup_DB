# Generated by Django 3.2.5 on 2022-03-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fond_main', '0003_rename_rt_ud_ticket_rt_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='blm_clx',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='defected_optical_cable_length',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='demontage_optical_cable_length',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='gpon_qty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hdmi_qty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='lan_cable_begin',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='lan_cable_code',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='lan_cable_end',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='lan_cable_length',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='optical_cable_begin',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='optical_cable_code',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='optical_cable_end',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='optical_cable_length',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='other_device_qty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='points',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='remote_control_qty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='service_link_measure',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='stb_qty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tower_working_time',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='wifi_router_qty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
