# Generated by Django 5.1.2 on 2024-10-25 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rascadores',
            old_name='descipcion_rascador',
            new_name='descripcion_rascador',
        ),
    ]