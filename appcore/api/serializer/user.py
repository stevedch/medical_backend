from rest_framework import serializers
from rest_framework.authtoken.models import Token

from appcore.models import User


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    @staticmethod
    def get_token(user):
        key_token = None
        try:
            Token.objects.get_or_create(user=user)
            key_token = Token.objects.get(user=user).key
        except Token.DoesNotExist:
            pass
        return 'Token {}'.format(key_token)
