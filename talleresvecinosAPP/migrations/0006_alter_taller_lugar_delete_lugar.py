# Generated by Django 5.2.1 on 2025-07-06 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talleresvecinosAPP', '0005_lugar_alter_taller_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taller',
            name='lugar',
            field=models.CharField(max_length=200, verbose_name='Lugar'),
        ),
        migrations.DeleteModel(
            name='Lugar',
        ),
    ]
