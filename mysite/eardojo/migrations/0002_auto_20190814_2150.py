# Generated by Django 2.0.13 on 2019-08-15 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eardojo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_text',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_title',
            field=models.CharField(max_length=100),
        ),
    ]
