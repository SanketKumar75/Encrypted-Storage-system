# Generated by Django 3.1.6 on 2021-02-10 12:32

from django.db import migrations, models
import django_two_factor_face_auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_two_factor_face_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfaceimage',
            name='image',
            field=models.ImageField(upload_to=django_two_factor_face_auth.models.content_file_name),
        ),
    ]