# Generated by Django 4.1.2 on 2023-03-13 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_alter_avataruser_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AvatarUser',
        ),
    ]
