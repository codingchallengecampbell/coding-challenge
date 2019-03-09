from rest_framework import generics, mixins


from postings.models import Post
from .serializers import PostSerializer



class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  
    lookup_field    = 'pk' 
    serializer_class = PostSerializer
    # queryset        = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class PostRudView(generics.RetrieveUpdateDestroyAPIView):
  
    lookup_field    = 'pk'
    serializer_class = PostSerializer
    # queryset        = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all()


