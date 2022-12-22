from rest_framework.viewsets import ModelViewSet

from bucsani_school.models import Post, GalleryImage, Document
from bucsani_school.serializers import PostSerializer, GallerySerializer, DocumentSerializer


class PostAPI(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GalleryAPI(ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GallerySerializer


class DocumentsAPI(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
