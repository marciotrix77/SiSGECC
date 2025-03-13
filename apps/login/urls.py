from django.urls import path, include
from login import views

app_name = 'login'

urlpatterns = [
    path('', views.login_view, name='login_SisGECC'), # Aponta a URL raiz para login_view
    path('logout', views.logout_view, name='logout'), # Adiciona a URL para a view de logout
]