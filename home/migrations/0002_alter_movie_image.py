# Generated by Django 3.2 on 2021-04-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='./movie'),
        ),
    ]
