# Generated by Django 3.0 on 2019-12-16 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DASE', '0005_auto_20191215_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beca_excelencia',
            name='aportante_fondo_becas',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='beca_excelencia',
            name='carrera',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='beca_excelencia',
            name='observaciones',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
