# Generated by Django 3.0.7 on 2020-07-09 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0010_auto_20200708_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='Projects',
        ),
    ]
