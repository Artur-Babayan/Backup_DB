# Generated by Django 3.2.5 on 2022-04-16 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fond_main', '0017_ticketmistake'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketmistake',
            options={'managed': True, 'ordering': ['ticket_mistake_name'], 'verbose_name_plural': 'TicketMistake'},
        ),
    ]