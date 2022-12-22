from django.contrib.auth import logout
from django.contrib.auth.models import Permission, Group
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.mixins import (
    RetrieveModelMixin,
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import User, Invite
from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    ChangePasswordSerializer,
    InviteSerializer,
    PermissionSerializer,
    GroupSerializer,
)


class GroupView(ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class PermissionView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()


class UserAPI(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# noinspection PyMethodMayBeStatic
class CurrentUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class ChangePasswordView(UpdateAPIView):
    model = User
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # If using drf authtoken, create a new token
        if hasattr(user, "auth_token"):
            user.auth_token.delete()
        token, created = Token.objects.get_or_create(user=user)
        # Return new token
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class GenerateInviteView(
    GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin
):
    serializer_class = InviteSerializer
    queryset = Invite.objects.all()


# class LoginView(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request, *args, **kwargs):
#         serializer = AuthTokenSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#
#         return Response({
#             'token': token.key,
#         })

# noinspection PyMethodMayBeStatic
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # request.user.auth_token.delete()  # Logout from everywhere
        logout(request)
        return Response("User Logged out successfully")


class SignupView(GenericViewSet, CreateModelMixin):
    serializer_class = UserCreateSerializer
    queryset = User.objects.none()
    permission_classes = [AllowAny]
