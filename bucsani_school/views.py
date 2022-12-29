from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from bucsani_school.models import Post, GalleryImage, Document, Description
from bucsani_school.serializers import PostSerializer, GallerySerializer, DocumentSerializer, DescriptionSerializer


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


class DescriptionAPI(ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
