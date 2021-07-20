from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django import forms
from django.contrib.auth.password_validation import validate_password
from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserSerializer


@permission_classes([])
class CadastroView(generics.CreateAPIView):
    """View para cadastrar usuario"""
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({"mensagem": "E necessario estar deslogado para cadastrar"})
        try:
            check_email(request)
            check_password(request)
            check_user(request)
        except Exception as e:
            return e.args[0]
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return Response({"mensagem": "Cadastro realizado"})
        return Response({"mensagem": "Usuario ja existente"})


class DeletarView(generics.DestroyAPIView):
    """View para deletar usuario"""
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        user.delete()
        return Response(status=202)


class EditarView(generics.UpdateAPIView):
    """View para editar usuario"""
    serializer_class = UserSerializer

    def patch(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        try:
            if request.data.get('username') is not None:
                check_user(request)
                user.username = request.data.get('username')
            if request.data.get('email') is not None:
                check_email(request)
                user.email = request.data.get('email')
            if request.data.get('password') is not None:
                check_password(request)
                user.password = make_password(request.data.get('password'))
        except Exception as e:
            return e.args[0]
        user.save()
        return Response({"mensagem": "pao"})


class LogoutView(APIView):
    """View para realizar o logout inserindo o token na blacklist"""
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token).blacklist()
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def check_email(request):
    """Validar Email obtida na requisição"""
    try:
        validate_email(request.data.get('email'))
    except forms.ValidationError:
        raise Exception(Response({"mensagem": "Digite um email no formato correto"}))


def check_password(request):
    """Validar senha obtida na requisição"""
    try:
        validate_password(request.data.get('password'))
    except:
        raise Exception(Response({"mensagem": "Digite uma senha no formato correto"}))


def check_user(request):
    """Validar usuario obtido na requisição"""
    print(len(request.data.get('username')))
    if len(request.data.get('username')) < 3:
        raise Exception(Response({"mensagem": "Digite um usuario correto"}))
