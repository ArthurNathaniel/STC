# Generated by Django 4.1.7 on 2023-05-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0002_alter_churchmember_children_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='churchmember',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=20),
        ),
    ]