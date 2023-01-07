from rest_framework.fields import SerializerMethodField, IntegerField
from rest_framework.serializers import ModelSerializer

from bucsani_school.models import Post, GalleryImage, PostImage, PostFile, Document, SiteConfig, PostType


class PostFileSerializer(ModelSerializer):
    class Meta:
        model = PostFile
        exclude = ['post']


class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        exclude = ['post']


class PostTypeSerializer(ModelSerializer):
    id = IntegerField(required=False)

    class Meta:
        model = PostType
        fields = "__all__"


class PostSerializer(ModelSerializer):
    images = SerializerMethodField(read_only=True)
    # images = PostImageSerializer(many=True, read_only=True)
    files = PostFileSerializer(many=True, required=False)
    type_id = IntegerField(required=False, write_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        depth = 1

    def get_images(self, obj: Post):
        return [PostImageSerializer(img, context=self.context).data['image'] for img in obj.images.all()]

    def get_files(self, obj: Post):
        return [PostFileSerializer(img, context=self.context).data['file'] for img in obj.files.all()]

    def create(self, validated_data):
        post_type = None
        post_type_pk: int = validated_data.pop("type_id", None)
        if post_type_pk:
            post_type = PostType.objects.get(pk=post_type_pk)

        post = self.Meta.model.objects.create(**validated_data, type=post_type)
        files = self.context['request'].FILES
        if files:
            try:
                for f in files.getlist('files'):
                    post.files.get_or_create(file=f)
            except Exception as e:
                print(e)

            try:
                for f in files.getlist('images'):
                    post.images.get_or_create(file=f)
            except Exception as e:
                print(e)
        return post

    def update(self, instance: Post, validated_data):
        post_type = None
        post_type_pk: int = validated_data.pop("type_id", None)
        if post_type_pk:
            post_type = PostType.objects.get(pk=post_type_pk)

        instance.type = post_type
        instance = super().update(instance, validated_data)
        files = self.context['request'].FILES
        if files:
            try:
                for f in files.getlist('files'):
                    instance.files.get_or_create(file=f)
            except Exception as e:
                print(e)

            try:
                for f in files.getlist('images'):
                    instance.images.get_or_create(file=f)
            except Exception as e:
                print(e)
        #PostType.objects.update_or_create(post=instance, pk=post_type_pk, defaults=post_type_data)
        return instance


class GallerySerializer(ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = "__all__"


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"


class SiteConfigSerializer(ModelSerializer):
    class Meta:
        model = SiteConfig
        exclude = ['id']
