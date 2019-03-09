from rest_framework import generics


from postings.models import Post
from .serializers import PostSerializer

class PostAPIView(generics.CreateAPIView):
  
    lookup_field    = 'pk' 
    serializer_class = PostSerializer
    # queryset        = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostRudView(generics.RetrieveUpdateDestroyAPIView):
  
    lookup_field    = 'pk'
    serializer_class = PostSerializer
    # queryset        = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all()


