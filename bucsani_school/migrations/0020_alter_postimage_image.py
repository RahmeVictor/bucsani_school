# Generated by Django 4.1.6 on 2023-02-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucsani_school', '0019_alter_galleryimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
