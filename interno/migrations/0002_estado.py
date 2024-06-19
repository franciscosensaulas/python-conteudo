# Generated by Django 5.0.6 on 2024-06-18 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('sigla', models.CharField(max_length=2, unique=True)),
            ],
        ),
    ]
