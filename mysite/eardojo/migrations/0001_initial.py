# Generated by Django 2.0.13 on 2019-08-15 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(max_length=60)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
