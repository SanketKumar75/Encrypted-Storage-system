# Generated by Django 3.1.6 on 2021-02-14 13:34

from django.db import migrations, models
import django_two_factor_face_auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_two_factor_face_auth', '0004_auto_20210213_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfaceimage',
            name='image',
            field=models.FileField(upload_to=django_two_factor_face_auth.models.content_file_name),
        ),
    ]
