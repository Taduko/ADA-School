from rest_framework import generics, permissions # Importamos generics y permissions
from .models import Post # Importamos el modelo Post
from .serializers import PostSerializer # Importamos el serializador PostSerializer
from django.shortcuts import render, get_object_or_404 # Importamos render y get_object_or_404

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})