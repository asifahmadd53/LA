# Generated by Django 5.0.4 on 2024-05-12 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_media/'),
        ),
    ]
