# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from appcore.api.serializer.user import UserSerializer
from appcore.models import User


class AuthViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @action(methods=['POST', ], detail=False, url_path='login')
    def login(self, request, *args, **kwargs):
        data = request.data

        user = None
        username = str(data.get('username'))
        password = str(data.get('password'))

        serializer = dict()
        response = dict(
            status=status.HTTP_400_BAD_REQUEST,
            content_type='application/json',
            headers=self.get_success_headers([])
        )

        try:
            user = self.queryset.get(username=username)
        except User.DoesNotExist as e:
            serializer = dict(message='El usuario %s ingresado no existe, por favor contáctese con el'
                                      ' administrador del sitio.' % username, data=None)

        if user is not None:
            user_auth = authenticate(username=username, password=password)
            if user_auth is not None:
                if user_auth.is_active:
                    login(request, user)

                    serializer = self.serializer_class(user).data
                    response = dict(
                        status=status.HTTP_202_ACCEPTED,
                        content_type='application/json',
                        headers=self.get_success_headers(serializer)
                    )

                    serializer = dict(
                        message=None,
                        data=serializer
                    )
                else:
                    serializer = dict(
                        message='El usuario %s ingresado no se encuentra activo, por favor contáctese con el'
                                ' administrador del sitio.' % username,
                        data=None
                    )
            else:
                serializer = dict(
                    message='El usuario o contraseña son incorrectos',
                    data=None
                )
        return Response(serializer, **response)

    @action(methods=['POST', ], detail=False, url_path='logout')
    def logout(self, request, *args, **kwargs):
        serializer = dict()
        response = dict(
            status=status.HTTP_400_BAD_REQUEST,
            content_type='application/json',
            headers=self.get_success_headers([])
        )
        try:
            logout(request)
            serializer = dict()
            response = dict(
                status=status.HTTP_202_ACCEPTED,
                content_type='application/json',
                headers=self.get_success_headers(serializer)
            )
        except Exception as e:
            pass

        return Response(serializer, **response)
