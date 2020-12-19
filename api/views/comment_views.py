from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.comment import Comment
from ..serializers import CommentSerializer

class Comments(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CommentSerializer
    def get(self, request):
      """Index request"""
      # Filter the comments by owner
      comments = Comment.objects.filter(owner=request.user.id)
      data = CommentSerializer(comments, many=True).data
      return Response(data)

    def post(self, request):
      """Create request"""
      request.data['comment']['owner'] = request.user.id
      comment = CommentSerializer(data=request.data['comment'])

      if comment.is_valid():
        comment.save()
        return Response(comment.data, status=status.HTTP_201_CREATED)
      else:
        return Response(comment.errors, status=status.HTTP_201_CREATED)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(IsAuthenticated,)
  def get(self, request, pk):
    """Show request"""
    comment = get_object_or_404(Comment, pk=pk)
    # Check if the user owns the comment
    if not request.user.id == comment.owner.id:
      raise PermissionDenied('Unauthorized, you do not own this comment')

    data = CommentSerializer(comment).data
    return Response(data)

  def delete(self, request, pk):
    """Delete request"""
    comment = get_object_or_404(Comment, pk=pk)

    if not comment.owner.id == request.user.id:
      raise PermissionDenied('Unauthorized, you do not own this comment')

    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def partial_update(self, request, pk):
    """Update request"""
    # remove the owner from the request object
    if request.data['comment'].get('owner', False):
      del request.data['comment']['owner']

    comment = get_object_or_404(Comment, pk=pk)
    post_id = comment.post_id.id
    print(comment.post_id.id)
    # check if the owner is the same as the user id
    if not request.user.id == comment.owner.id:
      raise PermissionDenied('Unauthorized, you do not own this comment')

    # Attach an owner to the request
    request.data['comment']['owner'] = request.user.id
    # To avoid having the user change the post id, set the post id in the comment
    request.data['comment']['post_id'] = post_id
    # request.data['comment']['post_id'] =
    data = CommentSerializer(comment, data=request.data['comment'])
    if data.is_valid():
      data.save()
      return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
