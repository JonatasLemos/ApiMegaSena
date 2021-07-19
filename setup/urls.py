from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from megasena.views import UltimoSorteioViewset,ListarJogosViewset,AcertosViewset
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register('ultimo-sorteio', UltimoSorteioViewset, basename='UltimoSorteio')
router.register('listar-jogos', ListarJogosViewset, basename='ListarJogos')
router.register('acertos', AcertosViewset, basename='Acertos')
# router.register('novo-jogo', NovoJogoViewset, basename='NovoJogo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('', include('megasena.urls')),
    path('', include('users.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
]
