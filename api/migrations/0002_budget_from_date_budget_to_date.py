# Generated by Django 4.2.17 on 2025-01-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='from_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='to_date',
            field=models.DateField(null=True),
        ),
    ]
