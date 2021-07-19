# Generated by Django 3.2.4 on 2021-07-15 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PranamsApp', '0018_add_demography_sssihms_pg_patient_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maintenance_Charges_Paid_Upto', models.CharField(blank=True, max_length=10, null=True, verbose_name='Maintenance Charges Paid Upto in MMM-YYYY')),
                ('Electricity_Charges_Paid_Upto', models.CharField(blank=True, max_length=10, null=True, verbose_name='Electrical Charges Paid Upto in MMM-YYYY')),
                ('Updated_Date', models.DateTimeField(auto_now_add=True)),
                ('Updated_By', models.CharField(default='Admin', max_length=10)),
                ('Status', models.CharField(default='Y', max_length=2)),
                ('Room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PranamsApp.room_master')),
            ],
        ),
    ]