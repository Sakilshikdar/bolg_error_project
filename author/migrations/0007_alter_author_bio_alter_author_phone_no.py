# Generated by Django 4.2.7 on 2023-12-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0006_alter_author_bio_alter_author_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='phone_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
