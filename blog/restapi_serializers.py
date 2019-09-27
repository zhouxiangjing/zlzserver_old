from rest_framework import serializers
from blog.models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'article', 'user', 'level', 'parent_id', 'created')
