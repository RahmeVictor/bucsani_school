# Generated by Django 4.1.4 on 2022-12-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bucsani_school", "0008_postfile_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="galleryimage",
            name="image",
            field=models.ImageField(upload_to="gallery"),
        ),
        migrations.AlterField(
            model_name="post",
            name="preview_image",
            field=models.ImageField(upload_to="media"),
        ),
        migrations.AlterField(
            model_name="postfile",
            name="file",
            field=models.FileField(upload_to="files"),
        ),
        migrations.AlterField(
            model_name="postimage",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
    ]
