# Generated by Django 4.0.4 on 2022-05-10 08:15

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='notes',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
    ]