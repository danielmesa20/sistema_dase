# Generated by Django 3.0 on 2019-12-21 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DASE', '0008_auto_20191221_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beca_excelencia',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='beca_excelencia',
            name='porcentaje',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='beca_excelencia',
            name='tipo_beneficio',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
