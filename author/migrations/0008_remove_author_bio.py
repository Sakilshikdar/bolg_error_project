# Generated by Django 4.2.7 on 2023-12-07 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0007_alter_author_bio_alter_author_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='bio',
        ),
    ]
