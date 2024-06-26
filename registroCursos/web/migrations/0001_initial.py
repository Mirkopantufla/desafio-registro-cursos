# Generated by Django 4.2 on 2024-05-25 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('modificacion_registro', models.DateField(auto_now=True)),
                ('creado_por', models.CharField(max_length=50)),
                ('cursos', models.ManyToManyField(related_name='profesores', to='web.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('modificacion_registro', models.DateField(auto_now=True)),
                ('creado_por', models.CharField(max_length=50)),
                ('cursos', models.ManyToManyField(related_name='estudiantes', to='web.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('dpto', models.CharField(max_length=10)),
                ('comuna', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('estudiante_id', models.OneToOneField(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='web.estudiante')),
            ],
        ),
    ]
