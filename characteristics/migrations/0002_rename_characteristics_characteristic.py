# Generated by Django 4.0.5 on 2022-06-13 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
        ('characteristics', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Characteristics',
            new_name='Characteristic',
        ),
    ]