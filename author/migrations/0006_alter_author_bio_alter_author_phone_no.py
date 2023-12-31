# Generated by Django 4.2.7 on 2023-12-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0005_remove_author_bio_remove_author_phone_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, default='No bio available', null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='phone_no',
            field=models.CharField(blank=True, default='No phone number available', max_length=12, null=True),
        ),
    ]
