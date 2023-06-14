# Generated by Django 3.2.5 on 2022-04-16 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fond_main', '0016_auto_20220404_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketMistake',
            fields=[
                ('ticket_mistake_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'ticket_mistake',
                'ordering': ['ticket_mistake_name'],
                'managed': True,
            },
        ),
    ]
