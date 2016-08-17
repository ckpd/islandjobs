from rest_framework import generics
from jobs.models import Jobpost
from .serializers import PostSerializer

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Jobpost.objects.all()
    serializer_class = PostSerializer
