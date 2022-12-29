from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from bucsani_school.models import Post, GalleryImage, PostImage, PostFile, Document, Description


class PostFileSerializer(ModelSerializer):
    class Meta:
        model = PostFile
        exclude = ['post']


class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        exclude = ['post']


class PostSerializer(ModelSerializer):
    images = SerializerMethodField(read_only=True)
    files = SerializerMethodField(read_only=True)

    # images = PostImageSerializer(many=True, read_only=True)
    # files = PostFileSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        depth = 1

    def get_images(self, obj: Post):
        return [PostImageSerializer(img, context=self.context).data['image'] for img in obj.images.all()]

    def get_files(self, obj: Post):
        return [PostFileSerializer(img, context=self.context).data['file'] for img in obj.files.all()]


class GallerySerializer(ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = "__all__"


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"


class DescriptionSerializer(ModelSerializer):
    class Meta:
        model = Description
        fields = "__all__"
