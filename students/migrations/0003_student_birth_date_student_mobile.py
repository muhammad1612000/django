# Generated by Django 4.2.1 on 2023-05-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_f_name_alter_student_l_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birth_date',
            field=models.DateField(default='2023-7-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.IntegerField(default=1122334455),
            preserve_default=False,
        ),
    ]
