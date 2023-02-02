from django.core.management import BaseCommand

from bucsani_school import models


class Command(BaseCommand):
    """Command that sets up the server. Run using Django's manage.py"""

    help = "Moves pictores from preview image to gallery, used in a migration, can be safley deleted"

    def handle(self, *args, **options):
        for post in models.Post.objects.all():
            preview_image = post.preview_image
            if preview_image:
                models.GalleryImage.objects.create(image=post.preview_image)
