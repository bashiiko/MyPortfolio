# Generated by Django 2.1 on 2019-12-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=10, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=255, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=10, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, verbose_name='username'),
        ),
    ]