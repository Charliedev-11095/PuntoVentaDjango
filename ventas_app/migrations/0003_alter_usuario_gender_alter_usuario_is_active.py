# Generated by Django 4.2.4 on 2023-08-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_app', '0002_usuario_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='gender',
            field=models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], max_length=9, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designa si este usuario debe tratarse como activo. Desactive este campo en lugar de eliminar usuarios.', verbose_name='Activo'),
        ),
    ]
