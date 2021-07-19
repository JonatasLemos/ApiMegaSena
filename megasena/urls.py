from django.urls import path
from . views import UltimoSorteioView,ListarJogosView,AcertosView,NovoJogoView

urlpatterns = [
    path('ultimo-sorteio', UltimoSorteioView.as_view(), name='ultimo_sorteio'),
    path('listar-jogos', ListarJogosView.as_view(), name='listar_jogos'),
    path('acertos', AcertosView.as_view(), name='acertos'),
    path('novo-jogo', NovoJogoView.as_view(), name='novo_jogo'),]
