# Generated by Django 2.2.13 on 2024-08-02 07:44

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
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('tools', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField()),
                ('img_name', models.CharField(max_length=100)),
            ],
        ),
    ]
