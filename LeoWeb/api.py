from .models import TagModel,ContentModel
from rest_framework import viewsets,permissions
from .serializer import TagSerializer,ContentSerializer

class TagViews(viewsets.ModelViewSet):
    queryset=TagModel.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=TagSerializer

class ContentViews(viewsets.ModelViewSet):
    queryset=ContentModel.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=ContentSerializer