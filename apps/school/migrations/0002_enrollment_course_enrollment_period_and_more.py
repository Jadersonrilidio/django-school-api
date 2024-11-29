# Generated by Django 5.0.3 on 2024-11-27 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.course'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='period',
            field=models.CharField(choices=[('M', 'Morming'), ('A', 'Afternoon'), ('N', 'Night')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student'),
        ),
    ]
