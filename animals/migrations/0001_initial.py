# Generated by Django 4.0.5 on 2022-06-13 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.FloatField()),
                ('weight', models.FloatField()),
                ('sex', models.CharField(max_length=15)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='animals.animal')),
            ],
        ),
    ]