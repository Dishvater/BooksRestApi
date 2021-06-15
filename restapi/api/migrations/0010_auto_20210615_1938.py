# Generated by Django 2.2 on 2021-06-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210615_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='average_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='ratings_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
