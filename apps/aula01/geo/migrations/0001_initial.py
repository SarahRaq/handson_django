# Generated by Django 2.1.7 on 2019-03-07 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=7, verbose_name='Código')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Município',
                'verbose_name_plural': 'Municípios',
            },
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('sigla', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='Sigla')),
                ('codigo', models.CharField(max_length=2, verbose_name='Código')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'UF',
                'verbose_name_plural': 'UFs',
            },
        ),
        migrations.AddField(
            model_name='municipio',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.UF'),
        ),
    ]
