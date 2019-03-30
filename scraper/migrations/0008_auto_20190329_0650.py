# Generated by Django 2.1.7 on 2019-03-28 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0007_remove_scrapingprocess_website_lists'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapingprocess',
            name='file_source',
        ),
        migrations.AddField(
            model_name='scrapingprocess',
            name='website_lists',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
