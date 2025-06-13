from rest_framework import viewsets
from .models import User, Profile, Action
from .serializers import UserSerializer, ProfileSerializer, ActionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

    @action(detail=False, methods=["get"], url_path="user/(?P<user_id>[^/.]+)")
    def actions_by_user(self, request, user_id=None):
        actions = Action.objects.filter(user__id=user_id).order_by('-timestamp')
        serializer = self.get_serializer(actions, many=True)
        return Response(serializer.data)
