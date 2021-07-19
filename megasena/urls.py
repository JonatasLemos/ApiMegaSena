from django.urls import path
from . views import NovoJogoView

urlpatterns = [
    path('novo', NovoJogoView, name='novo'),]
