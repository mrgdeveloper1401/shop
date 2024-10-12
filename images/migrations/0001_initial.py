# Generated by Django 5.1.2 on 2024-10-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("image_title", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(
                        height_field="image_height",
                        upload_to="images/%Y/%m/%d/",
                        width_field="image_width",
                    ),
                ),
                ("image_height", models.PositiveIntegerField(default=0)),
                ("image_width", models.PositiveIntegerField(default=0)),
                (
                    "image_hash",
                    models.CharField(max_length=40, verbose_name="image hash"),
                ),
                ("image_size", models.PositiveIntegerField(default=0)),
                (
                    "image_name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="image name"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
