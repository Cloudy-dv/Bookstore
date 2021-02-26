# Generated by Django 3.1.7 on 2021-02-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('pages', models.IntegerField(default=0)),
                ('art_cover', models.URLField(max_length=100)),
                ('published_lang', models.CharField(max_length=20)),
            ],
        ),
    ]
