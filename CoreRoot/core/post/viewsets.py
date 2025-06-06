from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core.abstract.viewsets import AbstractViewSet

from core.post.serializers import PostSerializer
from core.post.models import Post

class PostViewSet(AbstractViewSet):
    http_method_names = ('post','get','put','delete')
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
    
    def get_object(self):
        obj = Post.objects.get_object_by_public_id(
            self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response (serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)
        
from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.mthod is SAFE_METHODS
        
        if view.basename in ['post']:
            return bool (request.user and 
                         request.user.is_authenticated)
        return False

    def has_permission(self, request, view):
        if view.basename in ['post']:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            
            return bool (request.user and 
                         request.user.is_authenticated)
            
        return False
    
    
    