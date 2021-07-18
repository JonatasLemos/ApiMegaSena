import json
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.http import JsonResponse
from megasena.models import SorteioMegaSena
from megasena.megasena_scraper import MegaSenaDraw
from django.views import View

# Create your views here.
class UltimoSorteioView(View):
    def get(self,request):
        MegaSenaDraw()
        dict_obj = model_to_dict(SorteioMegaSena.objects.last())
        serialized = json.dumps(dict_obj,cls=DjangoJSONEncoder)
        load_json = json.loads(serialized)
        return JsonResponse(load_json,safe=False)
