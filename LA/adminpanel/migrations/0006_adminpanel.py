# Generated by Django 5.0.4 on 2024-05-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0005_delete_adminpanel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]