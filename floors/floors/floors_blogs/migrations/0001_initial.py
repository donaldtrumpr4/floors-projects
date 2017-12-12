# Generated by Django 2.0 on 2017-12-12 16:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
    ]