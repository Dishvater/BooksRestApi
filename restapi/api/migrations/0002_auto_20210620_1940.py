# Generated by Django 2.2 on 2021-06-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='categories',
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='api.Category'),
        ),
    ]
