# Generated by Django 4.0.4 on 2022-05-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MisFamiliares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='fechaDeNacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='yo',
            name='mifechaDeNacimiento',
            field=models.DateField(),
        ),
    ]
