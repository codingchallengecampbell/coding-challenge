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
        read_only_fields = ['user']
        # converts to Json
        # validates data

        def validate_title(self, value):
            qs = Post.objects.filter(title_iexact=value)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
                if qs.exists():
                    raise serializers.ValidationError("This title has already been used")
                    return value