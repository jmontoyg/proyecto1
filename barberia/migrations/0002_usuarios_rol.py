# Generated by Django 3.1.7 on 2021-04-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barberia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='rol',
            field=models.CharField(choices=[('1', 'Administrador'), ('2', 'Barbero'), ('3', 'Cliente')], default='3', max_length=1),
        ),
    ]