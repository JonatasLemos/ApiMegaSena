from django.urls import path
from . views import UltimoSorteioView

urlpatterns = [
    path('ultimo-sorteio', UltimoSorteioView.as_view(), name='ultimo_sorteio'),]
