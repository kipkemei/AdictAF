# Generated by Django 2.0.4 on 2018-05-11 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
