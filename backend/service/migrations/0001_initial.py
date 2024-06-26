# Generated by Django 5.0.6 on 2024-05-21 08:18

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Helpline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('hospital', 'Hospital'), ('fire_station', 'Fire Station'), ('police_station', 'Police Station')], max_length=100)),
                ('location_url', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward', models.IntegerField()),
                ('name', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('landmark', models.CharField(max_length=500)),
                ('problem_rate', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=10)),
                ('audio', cloudinary.models.CloudinaryField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaints', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='service.complaint')),
            ],
        ),
        migrations.CreateModel(
            name='HelplineImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255)),
                ('helpline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='service.helpline')),
            ],
        ),
    ]
