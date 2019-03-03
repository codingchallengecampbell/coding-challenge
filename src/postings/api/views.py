from rest_framework import generics


from postings.models import Post
from .serializers import PostSerializer

class PostRudView(generics.RetrieveUpdateDestroyAPIView):
  
    lookup_field    = 'pk'
    serializer_class = PostSerializer
    # queryset        = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all()

    # def get_object(self):
    #     return Post.objects.all()