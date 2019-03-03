from rest_framework import generics


from postings.models import Post
from .serializers import PostSerializer

class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field    = 'pk'
    serializer_class = Post
    # queryset        = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all()

    # def get_object(self):
    #     return Post.objects.all()