# Generated by Django 3.0.8 on 2020-07-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Artykuł',
                'verbose_name_plural': 'Artykuły',
            },
        ),
    ]
