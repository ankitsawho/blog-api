# Generated by Django 4.0.1 on 2022-01-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('posts', models.ManyToManyField(blank=True, related_name='categories', to='api.Post')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
