# Generated by Django 2.1.7 on 2019-03-28 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0006_remove_scrapingprocess_custom_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapingprocess',
            name='website_lists',
        ),
    ]
