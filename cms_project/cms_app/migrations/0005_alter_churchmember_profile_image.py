# Generated by Django 4.1.7 on 2023-06-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0004_churchmember_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='churchmember',
            name='profile_image',
            field=models.ImageField(default='N/A', upload_to='profile_images'),
        ),
    ]
