# Generated by Django 4.1.7 on 2023-03-04 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('url', models.CharField(blank=True, max_length=200, verbose_name='URL')),
                ('named_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='named_URL')),
                ('childes', models.ManyToManyField(blank=True, related_name='parents', to='menu.menu')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='HeadMenu',
            fields=[
                ('menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='menu.menu')),
                ('title', models.SlugField(verbose_name='Название меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]