# Generated by Django 3.0 on 2020-01-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DASE', '0013_auto_20191226_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='carrera',
            field=models.CharField(default='Nulo', max_length=100),
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='trimestre',
            field=models.CharField(default='Nulo', max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='tipo_beneficio',
            field=models.CharField(default='Nulo', max_length=100),
        ),
    ]
