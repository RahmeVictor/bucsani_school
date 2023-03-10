from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from bucsani_school.models import Post, GalleryImage, Document, SiteConfig, PostType, PostFile, PostImage
from bucsani_school.serializers import PostSerializer, GallerySerializer, DocumentSerializer, SiteConfigSerializer, \
    PostTypeSerializer, PostFileSerializer, PostImageSerializer


class PostAPI(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # parser_classes = (MultiPartParser, FormParser, JSONParser)

    # def list(self, request, *args, **kwargs):
    #     posts = self.get_queryset() # just did this as a test
    #     serializer = self.get_serializer(posts, many=True)
    #     return Response(serializer.data)


class PostTypeAPI(ModelViewSet):
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer


class PostFileAPI(ModelViewSet):
    queryset = PostFile.objects.all()
    serializer_class = PostFileSerializer


class PostImageAPI(ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer


class GalleryAPI(ModelViewSet):
    queryset = GalleryImage.objects.order_by('-pk')
    serializer_class = GallerySerializer


class DocumentsAPI(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class SiteConfigAPI(GenericViewSet, ListModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = SiteConfig.objects.all()
    serializer_class = SiteConfigSerializer

    def get_queryset(self):
        qs = SiteConfig.objects.all()
        if not qs.exists():
            configObj = SiteConfig.objects.create()
            configObj.save()

        return SiteConfig.objects.all()

    def list(self, request, *args, **kwargs):
        config = self.get_queryset().first()
        if config is None:
            configObj = SiteConfig.objects.create()
            configObj.save()
            serializer = self.get_serializer(configObj)
            return Response(serializer.data)

        serializer = self.get_serializer(config)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
