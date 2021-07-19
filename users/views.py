from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from users.serializers import UserSerializer
from rest_framework import generics

# @authentication_classes([])
@permission_classes([])
class CadastroView(generics.CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data = {
                "mensagem": "E necessario estar deslogado para cadastrar"
            }
            return Response(data)
        else:
            username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                data = {
                    "mensagem": "Cadastro realizado"
                }
                return Response(data)
            else:
                data = {
                    "mensagem": "Usuario ja existente"
                }
                return Response(data)

class DeletarView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    def delete(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        user.delete()
        return self.destroy(request, *args, **kwargs)
