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
        dict_obj = SorteioMegaSena.objects.order_by("-date").values()[0]
        print(type(dict_obj))
        # serialized = json.dumps(dict_obj,cls=DjangoJSONEncoder)
        # load_json = json.loads(serialized)
        return JsonResponse(dict_obj)
