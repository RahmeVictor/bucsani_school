# Generated by Django 4.1.4 on 2023-01-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bucsani_school", "0018_alter_siteconfig_background"),
    ]

    operations = [
        migrations.AlterField(
            model_name="galleryimage",
            name="image",
            field=models.ImageField(blank=True, upload_to="images"),
        ),
    ]
