from . views import NovoJogoView,UltimoSorteioViewset,ListarJogosViewset,AcertosViewset
from rest_framework import routers
from django.urls import path,include

urlpatterns = [
    path('novo', NovoJogoView.as_view(), name='novo')
]

megasena_router = routers.DefaultRouter()
megasena_router.register('ultimo-sorteio', UltimoSorteioViewset, basename='UltimoSorteio')
megasena_router.register('lista', ListarJogosViewset, basename='ListarJogos')
megasena_router.register('acertos', AcertosViewset, basename='Acertos')

