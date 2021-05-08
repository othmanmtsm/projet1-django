# Generated by Django 3.2 on 2021-05-08 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('roomType', models.CharField(choices=[('Single', 'Single Room'), ('Double', 'Double Room'), ('Triple', 'Triple Room'), ('Quad', 'Quad Room'), ('Queen', 'Queen Room'), ('King', 'King Room'), ('Twin', 'Twin Room'), ('Studio', 'Studio Room')], max_length=10)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('remise3j', models.DecimalField(decimal_places=2, max_digits=6)),
                ('remise8j', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
