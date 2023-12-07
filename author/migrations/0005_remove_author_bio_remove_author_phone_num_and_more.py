# Generated by Django 4.2.7 on 2023-12-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_alter_author_bio_alter_author_phone_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='Bio',
        ),
        migrations.RemoveField(
            model_name='author',
            name='phone_num',
        ),
        migrations.AddField(
            model_name='author',
            name='phone_no',
            field=models.CharField(default='No phone number available', max_length=12),
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(default='No bio available'),
        ),
    ]
