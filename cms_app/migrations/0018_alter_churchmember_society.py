# Generated by Django 4.1.7 on 2023-07-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0017_alter_churchmember_society'),
    ]

    operations = [
        migrations.AlterField(
            model_name='churchmember',
            name='society',
            field=models.CharField(max_length=700),
        ),
    ]
