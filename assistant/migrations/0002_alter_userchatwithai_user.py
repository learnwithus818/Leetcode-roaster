# Generated by Django 4.2 on 2024-06-21 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchatwithai',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
