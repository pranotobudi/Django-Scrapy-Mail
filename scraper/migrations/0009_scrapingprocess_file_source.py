# Generated by Django 2.1.7 on 2019-03-29 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0008_auto_20190329_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapingprocess',
            name='file_source',
            field=models.FileField(default='settings.MEDIA_ROOT/uploads/urls_backup.jpg', upload_to='uploads/'),
        ),
    ]