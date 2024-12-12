from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from acoes.models import Acoes
from dispositivos.models import Dispositivos
import json

def home(request):
    return render(request, 'dispositivos/home.html') 

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'dispositivos/cadastro.html')
    elif request.method == 'POST':
        nome = request.POST['nome']
        endereco = request.POST['endereco']
        chave = request.POST['chave']
        dispositivo = Dispositivos.objects.create(nome = nome, endereco = endereco, chave = chave)
        dispositivo.save()
        return redirect('listDevices')
    
def listagem(request):
    registros = Dispositivos.objects.all();
    return render(request, 'dispositivos/listagem.html', {'registros': registros}) 

def consulta(request):
    if request.method == "POST":
        try:
            id = request.POST['id']
            registros = Dispositivos.objects.get(pk=id) 
            return render(request, 'dispositivos/consulta.html', {'registro': registros})
        except Exception as ex:
            return render(request, 'dispositivos/consulta.html', {'erro': ex})
    else:   
        return render(request, 'dispositivos/consulta.html')

def excluir(request):
    registros = Dispositivos.objects.all()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            id = data['id']
            dispositivo = Dispositivos.objects.get(id=id)
            dispositivo.delete()
            return render(request, 'dispositivos/listagem.html', {'registros': registros}) 
        except Exception as ex:
            return render(request, 'dispositivos/listagem.html', {'mensagem': 'Erro ao excluir.'}, {'registros': registros}) 
    else:
        return render(request, 'dispositivos/listagem.html', {'registros': registros}) 
    
def atualizar(request, id):
    try:
        registro = Dispositivos.objects.get(id=id)
    except:
        return redirect('listDevices')       
    
    if request.method == "POST":
        registro.nome = request.POST['nome']
        registro.endereco = request.POST['endereco']
        registro.save()

        return redirect('listDevices')
    
    return render(request, 'dispositivos/atualizar.html', {'registro': registro})

def listagemAcoes(request, id):
    try:
        registro = Acoes.objects.filter(dispositivo=id)
    except Acoes.DoesNotExist:
        registro = None
    if request.method == "POST" and registro:
        registro.nome = request.POST.get('nome')
        registro.endereco = request.POST.get('endereco')
        registro.save()
        
        return render(request, 'acoes/listagem.html', {'registros': registro})

    return render(request, 'acoes/listagem.html', {'id': id, 
                  'registros': registro})

def cadastroAcao(request, id):
    if request.method == 'GET':
        try:
            dispositivo = Dispositivos.objects.get(id=id)
        except Dispositivos.DoesNotExist:
            return redirect('listActions')

        return render(request, 'acoes/cadastro.html', {'id': id, 'dispositivo': dispositivo})

    elif request.method == 'POST':
        acao = request.POST['acao']
        dispositivo = request.POST['dispositivo']
        acoes = Acoes.objects.create(acao=acao, dispositivo=dispositivo)
        acoes.save()
        
        return redirect('listActions', id=id)

    return redirect('listActions')

def excluirAcao(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            id = data['id']
            acao = Acoes.objects.get(id=id)
            acao.delete()
            return redirect('listActions', id=id) 
        except Exception as ex:
            return redirect('listDevices') 
    else:
        return redirect('listActions') 

def atualizarAcao(request, id):
    try:
        registro = Acoes.objects.get(id=id)
    except:
        return redirect('listActions', id=registro.dispositivo)       
    
    if request.method == "POST":
        registro.acao = request.POST['acao']
        registroDispositivo = registro.dispositivo
        registro.save()
        return redirect('listActions', id=registroDispositivo) 
    
    return render(request, 'acoes/atualizar.html', {'registro': registro})