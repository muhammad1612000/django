# Generated by Django 4.2.1 on 2023-05-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='f_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='l_name',
            field=models.CharField(max_length=255),
        ),
    ]