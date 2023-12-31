# Generated by Django 4.2.2 on 2023-06-20 05:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meeting_reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hrrepresentative',
            options={'verbose_name': 'hr representative', 'verbose_name_plural': 'hr representatives'},
        ),
        migrations.AddField(
            model_name='meetingreservation',
            name='parties',
            field=models.ManyToManyField(related_name='meeting_reservations_participations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meetingreservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_reservations', to=settings.AUTH_USER_MODEL),
        ),
    ]
