# Generated by Django 2.1 on 2019-12-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20191213_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Url（任意）'),
        ),
    ]
