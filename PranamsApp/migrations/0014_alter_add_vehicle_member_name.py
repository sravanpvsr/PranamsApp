# Generated by Django 3.2.4 on 2021-07-10 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PranamsApp', '0013_delete_vehicle_gate_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_vehicle',
            name='Member_Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PranamsApp.add_demography'),
        ),
    ]
