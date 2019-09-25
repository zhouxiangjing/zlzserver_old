
from rest_framework import viewsets
from blog.models import *
from blog.restapi_serializers import *


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
