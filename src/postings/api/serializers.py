from rest_framework import serializers

from postings.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'timestamp',
        ]

        # converts to Json
        # validates data