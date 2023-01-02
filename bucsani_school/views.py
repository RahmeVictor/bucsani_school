from rest_framework import status
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from bucsani_school.models import Post, GalleryImage, Document, SiteConfig
from bucsani_school.serializers import PostSerializer, GallerySerializer, DocumentSerializer, SiteConfigSerializer


class PostAPI(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def list(self, request, *args, **kwargs):
    #     posts = self.get_queryset() # just did this as a test
    #     serializer = self.get_serializer(posts, many=True)
    #     return Response(serializer.data)


class GalleryAPI(ModelViewSet):
    queryset = GalleryImage.objects.all()
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
