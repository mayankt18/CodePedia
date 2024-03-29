# Generated by Django 4.0.1 on 2022-01-07 14:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='snippet',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
