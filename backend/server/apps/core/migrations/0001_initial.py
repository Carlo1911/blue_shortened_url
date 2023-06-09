# Generated by Django 4.0.3 on 2023-03-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Original URL')),
                ('shortened_slug', models.CharField(max_length=100, unique=True, verbose_name='Shortened URL')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('total_visits', models.IntegerField(default=0, verbose_name='Total visits')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Shortened URL',
                'verbose_name_plural': 'Shortened URLs',
            },
        ),
    ]
