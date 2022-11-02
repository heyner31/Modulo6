# Generated by Django 4.1.1 on 2022-10-27 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=32, verbose_name='titulo')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha actualizacion')),
            ],
        ),
    ]
