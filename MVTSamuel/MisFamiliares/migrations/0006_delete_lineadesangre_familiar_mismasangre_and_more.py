# Generated by Django 4.0.4 on 2022-05-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MisFamiliares', '0005_familiar_edad_yo_miedad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LineaDeSangre',
        ),
        migrations.AddField(
            model_name='familiar',
            name='mismaSangre',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='familiar',
            name='relacion',
            field=models.CharField(default='', max_length=20),
        ),
    ]