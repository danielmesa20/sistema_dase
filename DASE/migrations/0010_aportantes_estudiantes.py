# Generated by Django 3.0 on 2019-12-27 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DASE', '0009_auto_20191221_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='estudiantes',
            fields=[
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_beneficio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='aportantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_aportante', models.CharField(max_length=100)),
                ('trimestre', models.CharField(max_length=10)),
                ('cedula_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DASE.estudiantes')),
            ],
        ),
    ]
