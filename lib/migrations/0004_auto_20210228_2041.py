# Generated by Django 3.1.7 on 2021-02-28 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0003_auto_20210228_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='art_cover',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='books',
            name='isbn',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='published_lang',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]