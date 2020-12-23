from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.post import Post
from ..serializers import UAPostSerializer, UAPostReadSerializer

# Post unauthenticated views
class APosts(generics.ListAPIView):
  permission_classes=()
  def get(self, request):
    """Index request"""
    posts = Post.objects.all()
    data = UAPostSerializer(posts, many=True).data
    return Response(data)

class UnauthenticatedPostDetail(generics.RetrieveAPIView):
  permission_classes=()
  def get(self, request, pk):
    """Show request"""
    post = get_object_or_404(Post, pk=pk)
    data = UAPostReadSerializer(post).data
    return Response(data)
