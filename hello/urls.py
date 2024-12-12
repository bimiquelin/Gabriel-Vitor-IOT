from django.contrib import admin
from django.urls import path
from dispositivos import views as view
from hello import views 
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('dispositivos/', view.home),
    path('dispositivos/add', view.cadastro, name='addDevice'),
    path('dispositivos/list', view.listagem, name='listDevices'),
    path('dispositivos/del', view.excluir, name='delDevice'),
    path('dispositivos/upd/<int:id>/', view.atualizar, name='updDevice'),
    path('acoes/list/<int:id>/', view.listagemAcoes, name='listActions'),
    path('acoes/add/<int:id>/', view.cadastroAcao, name='addAction'),
    path('acoes/del', view.excluirAcao, name='delAction'),
    path('acoes/upd/<int:id>/', view.atualizarAcao, name='updAction'),
]
