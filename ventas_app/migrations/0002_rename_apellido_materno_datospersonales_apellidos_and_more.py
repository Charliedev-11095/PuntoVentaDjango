# Generated by Django 4.2.3 on 2023-08-02 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datospersonales',
            old_name='apellido_materno',
            new_name='apellidos',
        ),
        migrations.RemoveField(
            model_name='datospersonales',
            name='apellido_paterno',
        ),
    ]