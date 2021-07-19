from django.urls import path
from .views import CadastroView

urlpatterns = [
    path('cadastro', CadastroView.as_view(), name='cadastro'),
    # path('deletar', DeletarView.as_view(), name='deletar'),
]