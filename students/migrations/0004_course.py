# Generated by Django 4.2.1 on 2023-05-14 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_birth_date_student_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=255)),
                ('l_name', models.CharField(max_length=255)),
            ],
        ),
    ]
