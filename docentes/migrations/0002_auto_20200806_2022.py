# Generated by Django 3.0.8 on 2020-08-07 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docentes',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='docentes',
            name='user',
            field=models.CharField(max_length=200, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='docentes',
            name='user_mod',
            field=models.CharField(max_length=15, verbose_name='user_mod'),
        ),
    ]
