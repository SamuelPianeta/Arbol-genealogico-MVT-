# Generated by Django 4.0.4 on 2022-05-29 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MisFamiliares', '0004_remove_familiar_apellido_remove_familiar_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='Edad',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='yo',
            name='miEdad',
            field=models.IntegerField(default=1),
        ),
    ]
