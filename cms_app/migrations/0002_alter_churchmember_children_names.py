# Generated by Django 4.1.7 on 2023-05-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='churchmember',
            name='children_names',
            field=models.TextField(blank=True, null=True),
        ),
    ]