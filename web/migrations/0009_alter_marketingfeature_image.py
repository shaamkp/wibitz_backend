# Generated by Django 3.2.9 on 2021-11-23 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_marketingfeature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingfeature',
            name='image',
            field=models.FileField(upload_to='marketingFeatures/'),
        ),
    ]
