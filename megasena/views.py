from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from megasena.models import SorteioMegaSena, NovoJogo
from megasena.megasena_scraper import MegaSenaDraw
from megasena.serializers import SorteioMegaSenaSerializer, NovoJogoSerializer, AcertosSerializer, \
    NovoJogoDezenasSerializer
from megasena.sorteio import Jogo


class UltimoSorteioViewset(viewsets.ReadOnlyModelViewSet):
    """Viewset do endpoint contendo o ultimo sorteio da megasena"""
    permission_classes = (IsAuthenticated,)
    MegaSenaDraw()

    def get_queryset(self):
        ultimo_sorteio = SorteioMegaSena.objects.order_by("-id").values()[0]
        queryset = SorteioMegaSena.objects.filter(id=ultimo_sorteio["id"])
        return queryset

    serializer_class = SorteioMegaSenaSerializer


class ListarJogosViewset(viewsets.ReadOnlyModelViewSet):
    """Viewset do endpoint contendo a lista de ultimos jogos do usuario"""
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = NovoJogo.objects.filter(user_id=self.request.user.id)
        return queryset

    serializer_class = NovoJogoSerializer


class AcertosViewset(viewsets.ReadOnlyModelViewSet):
    """Viewset do endpoint com o numero de acertos no ultimo jogo do usuario"""
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        game_list = NovoJogo.objects.filter(user_id=self.request.user.id)
        if len(game_list) != 0:
            acertos = NovoJogo.objects.filter(user_id=self.request.user.id).order_by("-id").values()[0]
            queryset = NovoJogo.objects.filter(id=acertos["acertos"])
            return queryset
        queryset = []
        return queryset

    serializer_class = AcertosSerializer


class NovoJogoView(generics.CreateAPIView):
    """Criar um novo jogo com quantidade de dezenas escolhida pelo usuario"""
    permission_classes = (IsAuthenticated,)
    serializer_class = NovoJogoDezenasSerializer

    def post(self, request, *args, **kwargs):
        dezenas = int(request.data.get('dezenas'))
        usuario = request.user
        if 6 <= dezenas <= 10:
            Jogo(dezenas, usuario)
            return Response({"message": f"Jogo com {dezenas} dezenas criado"})
        else:
            return Response({"message": "A dezena deve estar entre 6 e 10"})
