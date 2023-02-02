from django.contrib.auth import password_validation
from django.contrib.auth.models import Permission, Group
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    ValidationError,
)

from .models import User
from .utils import get_user_token


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ["id", "name", "codename"]


# noinspection PyMethodMayBeStatic
class UserSerializer(ModelSerializer):
    token = SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "salary",
            "groups",
            "user_permissions",
            "is_active",
            "is_superuser",
            "is_staff",
            "token",
        ]

    def get_token(self, obj: User) -> str:
        if self.context["request"].user == obj:
            return get_user_token(obj)
        else:
            return ""


# noinspection PyMethodMayBeStatic
class UserCreateSerializer(ModelSerializer):
    token = SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
            "user_permissions",
            "password",
            "token",
        ]
        read_only_fields = ["is_staff", "is_superuser", "user_permissions"]
        extra_kwargs = {"password": {"write_only": True}}

    def get_token(self, obj: User) -> str:
        return get_user_token(obj)

    # def validate_email(self, value):
    #     if not Invite.objects.filter(email__exact=value).exists():
    #         raise ValidationError("email not invited")
    #
    #     return value

    def validate_password(self, value):
        password_validation.validate_password(value, self.context["request"].user)
        return value

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(self.validated_data["password"])
        user.save()
        return user


class ChangePasswordSerializer(Serializer):  # noqa
    """
    Serializer for password change endpoint.
    """

    model = User
    old_password = CharField(required=True)
    new_password = CharField(required=True)

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise ValidationError("Old password was entered incorrectly")

        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value, self.context["request"].user)
        return value

    def save(self, **kwargs):
        password = self.validated_data["new_password"]
        user = self.context["request"].user
        user.set_password(password)
        user.save()
        return user
