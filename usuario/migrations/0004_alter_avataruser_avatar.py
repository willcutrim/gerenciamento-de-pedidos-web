# Generated by Django 4.1.2 on 2023-02-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avataruser',
            name='avatar',
            field=models.ImageField(upload_to='Image/'),
        ),
    ]
