# Generated by Django 3.2.8 on 2022-03-16 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
    ]
