# Generated by Django 3.0.7 on 2020-07-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='certifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CertName', models.TextField(max_length=50)),
                ('Cert_Image', models.ImageField(upload_to='images/')),
                ('Issued_By', models.TextField(max_length=25)),
            ],
        ),
    ]
