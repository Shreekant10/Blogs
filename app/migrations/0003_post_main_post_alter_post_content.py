# Generated by Django 5.1.4 on 2024-12-27 16:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="main_post",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
