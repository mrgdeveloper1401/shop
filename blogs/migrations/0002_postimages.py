# Generated by Django 5.1.2 on 2024-10-12 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_publish", models.BooleanField(default=True)),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="fk_post_images_image",
                        to="images.image",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="fk_post_images_post",
                        to="blogs.post",
                    ),
                ),
            ],
            options={
                "verbose_name": "post image",
                "verbose_name_plural": "post images",
                "db_table": "post_image",
            },
        ),
    ]
