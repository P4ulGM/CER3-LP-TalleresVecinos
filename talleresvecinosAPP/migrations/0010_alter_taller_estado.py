# Generated by Django 5.2.1 on 2025-07-06 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talleresvecinosAPP', '0009_categoria_alter_taller_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taller',
            name='estado',
            field=models.CharField(choices=[('aceptado', 'Aceptado'), ('pendiente', 'Pendiente'), ('rechazado', 'Rechazado')], default='pendiente', max_length=20, verbose_name='Estado'),
        ),
    ]
