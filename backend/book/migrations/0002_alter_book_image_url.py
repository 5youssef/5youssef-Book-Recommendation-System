# Generated by Django 5.0.7 on 2024-07-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]
