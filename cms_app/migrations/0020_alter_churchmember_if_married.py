# Generated by Django 4.1.7 on 2023-07-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0019_alter_churchmember_children_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='churchmember',
            name='if_married',
            field=models.CharField(choices=[('None', 'None'), ('Holy Matrimony', 'Holy Matrimony'), ('Traditional Marriage', 'Traditional Marriage')], max_length=100),
        ),
    ]
