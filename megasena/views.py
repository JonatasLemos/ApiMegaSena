from rest_framework.decorators import api_view
from rest_framework.response import Response
from megasena.models import SorteioMegaSena,NovoJogo
from megasena.megasena_scraper import MegaSenaDraw
from megasena.serializers import SorteioMegaSenaSerializer,NovoJogoSerializer,AcertosSerializer,NovoJogoDezenasSerializer
from megasena.sorteio import Jogo
from rest_framework import viewsets

class UltimoSorteioViewset(viewsets.ReadOnlyModelViewSet):
    MegaSenaDraw()
    def get_queryset(self):
        a = SorteioMegaSena.objects.order_by("-id").values()[0]
        queryset = SorteioMegaSena.objects.filter(id=a["id"])
        return queryset
    serializer_class = SorteioMegaSenaSerializer


class ListarJogosViewset(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        queryset = NovoJogo.objects.filter(user_id=self.request.user.id)
        return queryset
    serializer_class = NovoJogoSerializer


class AcertosViewset(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        a = NovoJogo.objects.filter(user_id=self.request.user.id).order_by("-id").values()[0]
        queryset = NovoJogo.objects.filter(id=a["id"])
        return queryset
    serializer_class = AcertosSerializer

@api_view(['GET','POST'])
def NovoJogoView(request):
    if request.method == 'POST':
        dezenas = int(request.data.get('dezenas'))
        if dezenas >= 6 and dezenas <= 10:
            Jogo(dezenas)
            return Response({"message": f"Jogo com {dezenas} dezenas criado"})
        else:
            return Response({"message": "A dezena deve estar entre 6 e 10"})
    return Response({"message": "Entre um jogo com dezenas entre 6 e 10"})
