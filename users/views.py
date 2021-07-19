from django.shortcuts import render
from django.contrib.auth.models import User
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class CadastroView(View):
    def post(self,request):
        data = json.loads(request.body.decode("utf-8"))
        usuario = data.get('usuario')
        email = data.get('email')
        senha = data.get('senha')
        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(username=usuario, email=email, password=senha)
            user.save()
            data = {
                "message": "Usuario cadastrado com sucesso" }
            return JsonResponse(data)
        else:
            data = {
                "message": "Email ja existe" }
            return JsonResponse(data)