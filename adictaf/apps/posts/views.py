from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from django.shortcuts import get_object_or_404
from . import serializers as sz
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status
from noire.bot.base import NoireBot
import logging
from rest_framework.permissions import AllowAny

logger = logging.getLogger(__name__)

class PostViewset(viewsets.ModelViewSet):
    serializer_class = sz.PostSerializer
    queryset = Post.objects.all()

from adictaf.apps.core.models import Project
from .tasks import load_user_posts
class UserViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = sz.PostSerializer(post)
        # if serializer.is_valid():
        return Response(serializer.data)
        # return Response(serializer.errors)

    @transaction.atomic()
    def update(self, request, pk=None):
        try:
            post = Post.objects.select_for_update().get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "No such post"}, status=status.HTTP_404_NOT_FOUND)
from rest_framework.decorators import permission_classes, api_view
from adictaf.utilities.permissions import AdictAFAdminOrReadOnly

@api_view(['POST'])
# @permission_classes([AdictAFAdminOrReadOnly])
@permission_classes([AllowAny])
def crawl_username(request):
    if not 'username' in request.data:
        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
    username=request.data['username']
    logger.info('Loading user posts for {0}'.format(username))
    proj = Project.objects.filter(active=True).last()
    try:
        bot = NoireBot(proj.username, proj.get_password)
    except AttributeError:
        logger.error("No active project in db")
        return
    usernameid = bot.convert_to_user_id(username)
    load_user_posts.delay(usernameid)
    return Response({"success": "data is being loaded"})
