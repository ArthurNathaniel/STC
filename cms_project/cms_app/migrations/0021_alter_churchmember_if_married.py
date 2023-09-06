# Generated by Django 4.1.7 on 2023-07-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0020_alter_churchmember_if_married'),
    ]

    operations = [
        migrations.AlterField(
            model_name='churchmember',
            name='if_married',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Holy Matrimony', 'Holy Matrimony'), ('Traditional Marriage', 'Traditional Marriage')], max_length=100),
        ),
    ]
