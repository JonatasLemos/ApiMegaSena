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
class RegistroView(View):
    def post(self,request):
        pass
        #     user = User.objects.create_user(username="john", email="john@gmail.com", password="1232")
        #     user.save()
        #     dict_obj = model_to_dict(User.objects.last())
        #     serialized = json.dumps(dict_obj, cls=DjangoJSONEncoder)
        #     load_json = json.loads(serialized)
        #     return JsonResponse(load_json, safe=False)