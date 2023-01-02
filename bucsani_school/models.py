from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField, ImageField, ManyToManyField, ForeignKey, CASCADE, FileField,
)


class PostType(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(Model):
    preview_image = ImageField(upload_to='media')
    title = CharField(max_length=250)
    author = CharField(max_length=100)
    body = TextField()
    type = ManyToManyField(PostType)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(Model):
    image = ImageField(upload_to='images')
    post = ForeignKey(Post, on_delete=CASCADE, related_name='images')

    def __str__(self):
        return self.image.name


class PostFile(Model):
    file = FileField(upload_to='files')
    post = ForeignKey(Post, on_delete=CASCADE, related_name='files')

    def __str__(self):
        return self.file.name


class GalleryImage(Model):
    image = ImageField(upload_to='gallery')

    def __str__(self):
        return self.image.name


class Document(Model):
    document = FileField(upload_to='documents')

    def __str__(self):
        return self.document.name


class SiteConfig(Model):
    background = ImageField(upload_to='internal')
    description = TextField()
    contact = TextField()

    def __str__(self):
        return "Site configuration"
