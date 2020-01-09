# Generated by Django 3.0 on 2019-12-27 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DASE', '0010_aportantes_estudiantes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aportantes',
            name='cedula_fk',
        ),
        migrations.AddField(
            model_name='aportantes',
            name='cedula_fk',
            field=models.ManyToManyField(to='DASE.estudiantes'),
        ),
        migrations.AlterField(
            model_name='aportantes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
