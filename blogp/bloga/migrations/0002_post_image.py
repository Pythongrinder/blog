# Generated by Django 2.2.2 on 2019-06-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='spaday.jpg', upload_to='media/'),
        ),
    ]
