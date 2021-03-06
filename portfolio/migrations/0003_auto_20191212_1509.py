# Generated by Django 2.1 on 2019-12-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20191209_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(max_length=255, verbose_name='url'),
        ),
    ]
