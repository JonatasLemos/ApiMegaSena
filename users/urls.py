from django.urls import path
from .views import CadastroView,DeletarView,EditarView,LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('cadastro', CadastroView.as_view(), name='cadastro'),
    path('deletar', DeletarView.as_view(), name='deletar'),
    path('editar', EditarView.as_view(), name='editar'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutView.as_view(), name='auth_logout'),
]