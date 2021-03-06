# Generated by Django 2.2 on 2021-06-16 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('published_date', models.CharField(max_length=10, null=True)),
                ('average_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('ratings_count', models.IntegerField(blank=True, null=True)),
                ('thumbnail', models.CharField(max_length=256, null=True)),
                ('bookid', models.CharField(max_length=32, unique=True)),
                ('authors', models.ManyToManyField(blank=True, null=True, to='api.Author')),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Category')),
            ],
        ),
    ]
