# Generated by Django 4.2 on 2023-04-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_operationtype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationtype',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Тип операции'),
        ),
    ]
