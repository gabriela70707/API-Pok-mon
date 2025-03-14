from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.read_pokemon), #name da um nome para o caminho, nesse caso nao precisa pq nao vamos usa-lo em nenhum html
    path('api/<int:pk>', views.read_one_pokemon),
    path('api/criar', views.create_pokemon),
    path('api/alterar/<int:pk>', views.update_pokemon),
    path('api/deletar/<int:pk>', views.delete_pokemon)
]