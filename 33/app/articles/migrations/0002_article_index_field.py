# Generated by Django 3.0.8 on 2020-07-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='index_field',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
