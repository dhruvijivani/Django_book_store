# Generated by Django 3.1.5 on 2021-01-30 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210129_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.CharField(default='', max_length=200, null=True, unique=True),
        ),
    ]