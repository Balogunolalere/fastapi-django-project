# Generated by Django 4.1 on 2022-08-10 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UpdateItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True, verbose_name='Slug')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
            ],
            options={
                'verbose_name': 'UpdateItem',
                'verbose_name_plural': 'UpdateItems',
                'ordering': ('name',),
            },
        ),
    ]
