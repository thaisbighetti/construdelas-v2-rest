# Generated by Django 4.0.5 on 2022-07-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('rg', models.CharField(max_length=11)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]