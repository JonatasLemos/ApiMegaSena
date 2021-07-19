import json
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from megasena.models import SorteioMegaSena,NovoJogo
from megasena.megasena_scraper import MegaSenaDraw
from megasena.sorteio import Jogo
from django.views import View
from django.core.serializers import serialize

# Create your views here.
class UltimoSorteioView(View):
    def get(self,request):
        MegaSenaDraw()
        ultimo_sorteio = SorteioMegaSena.objects.order_by("-id").values()[0]
        # ultimo_sorteio_serialized = serialize('python', ultimo_sorteio,cls=DjangoJSONEncoder)
        data = {"Ultimo sorteio da megasena":ultimo_sorteio}
        # serialized = simplejson.dumps(ultimo_sorteio,cls=DjangoJSONEncoder)
        # load_json = simplejson.loads(serialized)
        return JsonResponse(data)

class ListarJogosView(View):
    def get(self,request):
        jogos = NovoJogo.objects.filter(user_id=request.user.id)
        jogos_serialized = serialize('python', jogos)
        jogos_serialized_clean = [d['fields'] for d in jogos_serialized]
        data = {
            "Jogos passados": jogos_serialized_clean,
        }
        # print(type(dict_obj))
        # serialized = json.dumps(dict_obj,cls=DjangoJSONEncoder)
        # load_json = json.loads(serialized)
        return JsonResponse(data)

class AcertosView(View):
    def get(self,request):
        jogos = NovoJogo.objects.filter(user_id=request.user.id).order_by("-id").values()[0]
        data = {
            "Numero de dezenas certas no ultimo jogo": jogos["acertos"],
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class NovoJogoView(View):
    def post(self,request):
        MegaSenaDraw()
        data = json.loads(request.body.decode("utf-8"))
        dezenas = data.get('dezenas')
        user_id = data.get('user_id')
        if dezenas >= 6 and dezenas <= 10:
            Jogo(dezenas)
            jogos = NovoJogo.objects.filter(user_id=user_id).order_by("-id").values()[0]
            data = {
                "Novo jogo": jogos
            }
            return JsonResponse(data,status=201)
        else:
            data = {
                "message": "O numero de dezenas deve estar entre 6 e 10"
            }
            return JsonResponse(data)

