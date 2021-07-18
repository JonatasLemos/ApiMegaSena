import json
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.http import JsonResponse
from megasena.models import SorteioMegaSena
from megasena.last_result import update_last_draw

# Create your views here.
def ultimo_sorteio(request):
    if request.method == 'GET':
        update_last_draw()
        dict_obj = model_to_dict(SorteioMegaSena.objects.last())
        serialized = json.dumps(dict_obj,cls=DjangoJSONEncoder)
        load_json = json.loads(serialized)
        return JsonResponse(load_json,safe=False)
