# Generated by Django 5.1.2 on 2024-10-12 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0002_postimages"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="title_post",
            new_name="post_title",
        ),
    ]
