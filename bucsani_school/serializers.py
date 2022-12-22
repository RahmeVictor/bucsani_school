from rest_framework.serializers import ModelSerializer

from bucsani_school.models import Post, GalleryImage, PostImage, PostFile, Document


class PostFileSerializer(ModelSerializer):
    class Meta:
        model = PostFile
        exclude = ['post']


class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        exclude = ['post']


class PostSerializer(ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    files = PostFileSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        depth = 1


class GallerySerializer(ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = "__all__"


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
