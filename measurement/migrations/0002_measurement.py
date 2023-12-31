# Generated by Django 4.2.5 on 2023-10-12 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=1, max_digits=8)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meas', to='measurement.sensor')),
            ],
        ),
    ]
