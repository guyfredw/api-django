from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.post import Post
from ..serializers import PostSerializer

# Post views
class Posts(generics.ListCreateAPIView):
  permission_classes=(IsAuthenticated,)
  serializer_class = PostSerializer
  def get(self, request):
    """Index request"""
    posts = Post.objects.filter(owner = request.user.id)
    data = PostSerializer(posts, many=True).data
    return Response(data)


  def post(self, request):
    """Create request"""
    # set the user id as the owner of the post
    request.data['post']['owner'] = request.user.id

    # Serialze/create post
    post = PostSerializer(data=request.data['post'])
    if post.is_valid():
      p = post.save()
      return Response(post.data, status=status.HTTP_201_CREATED)
    else:
      return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(IsAuthenticated,)
  def get(self, request, pk):
    """Show request"""
    post = get_object_or_404(Post, pk=pk)
    # show owned post
    if not request.user.id == post.owner.id:
      raise PermissionDenied('Unauthorized, you do not own this post')

    data = PostSerializer(post).data
    return Response(data)

  def delete(self, request, pk):
    """Delete request"""
    post = get_object_or_404(Post, pk=pk)

    if not post.owner.id == request.user.id:
      raise PermissionDenied('Unauthorized, you do not own this post')

    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def partial_update(self, request, pk):
    """Update request"""
    # Remove owner from request object
    if request.data['post'].get('owner', False):
      del request.data['post']['owner']

    post = get_object_or_404(Post, pk=pk)

    # check if the owner is the same as the user id
    if not request.user.id == post.owner.id:
      raise PermissionDenied('Unauthorized, you do not own this post')

    # Attach an owner to the request
    request.data['post']['owner'] = request.user.id

    data = PostSerializer(post, data=request.data['post'])
    if data.is_valid():
      data.save()
      return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
