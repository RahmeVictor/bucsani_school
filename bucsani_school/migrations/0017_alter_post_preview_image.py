# Generated by Django 4.1.4 on 2023-01-08 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bucsani_school", "0016_alter_postimage_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="preview_image",
            field=models.FileField(upload_to="preview_images"),
        ),
    ]
