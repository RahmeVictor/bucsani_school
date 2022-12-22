from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from bucsani_school.models import Post, GalleryImage, Document
from bucsani_school.serializers import PostSerializer, GallerySerializer, DocumentSerializer


class PostAPI(ListModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def list(self, request, *args, **kwargs):
    #     posts = self.get_queryset() # just did this as a test
    #     serializer = self.get_serializer(posts, many=True)
    #     return Response(serializer.data)


class GalleryAPI(ListModelMixin, GenericViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GallerySerializer


class DocumentsAPI(ListModelMixin, GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
