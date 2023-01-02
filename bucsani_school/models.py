from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField, ManyToManyField, ForeignKey, CASCADE, FileField, URLField
)


class PostType(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(Model):
    preview_image = URLField(blank=True)
    title = CharField(max_length=250)
    author = CharField(max_length=100)
    body = TextField()
    type = ManyToManyField(PostType)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(Model):
    image = URLField(blank=True)
    post = ForeignKey(Post, on_delete=CASCADE, related_name='images')

    def __str__(self):
        return self.post.title


class PostFile(Model):
    file = FileField(upload_to='files')
    post = ForeignKey(Post, on_delete=CASCADE, related_name='files')

    def __str__(self):
        return self.file.name


class GalleryImage(Model):
    image = URLField(blank=True)


class Document(Model):
    document = FileField(upload_to='documents')

    def __str__(self):
        return self.document.name


class SiteConfig(Model):
    background = URLField(blank=True)
    description = TextField(blank=True)
    contact = TextField(blank=True)

    def __str__(self):
        return "Site configuration"
