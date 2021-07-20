from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from megasena.urls import megasena_router

router_config = routers.DefaultRouter()
router_config.get_api_root_view().cls.__name__ = "Api Megasena"
router_config.get_api_root_view().cls.__doc__ = "Api para simular jogos e comparar com o ultimo sorteio da Megasena"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(megasena_router.urls)),
    path('jogo/', include('megasena.urls')),
    path('usuario/', include('users.urls')),
]
