# Generated by Django 3.0 on 2019-12-15 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DASE', '0003_auto_20191215_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beca_excelencia',
            name='aportante_fondo_becas',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='beca_excelencia',
            name='observaciones',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]