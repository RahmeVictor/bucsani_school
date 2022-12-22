from rest_framework.authtoken.models import Token

from users.models import User


def get_user_token(user: User) -> str:
    return Token.objects.get_or_create(user=user)[0].key
