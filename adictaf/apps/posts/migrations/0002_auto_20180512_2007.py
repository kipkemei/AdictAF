# Generated by Django 2.0.4 on 2018-05-12 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
