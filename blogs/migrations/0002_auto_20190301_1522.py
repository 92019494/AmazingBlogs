# Generated by Django 2.1.5 on 2019-03-01 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='blog',
            new_name='body',
        ),
    ]
