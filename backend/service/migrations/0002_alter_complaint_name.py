# Generated by Django 5.0.6 on 2024-05-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
