# Generated by Django 2.2.6 on 2019-10-19 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mass', models.DecimalField(blank=True, decimal_places=4, max_digits=50)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sun', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sun', to='sim.Sun')),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mass', models.DecimalField(blank=True, decimal_places=4, max_digits=50)),
                ('start_x', models.DecimalField(blank=True, decimal_places=4, max_digits=10)),
                ('start_y', models.DecimalField(blank=True, decimal_places=4, max_digits=10)),
                ('sun', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='of_sun', to='sim.Sun')),
            ],
        ),
    ]