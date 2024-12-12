from django.shortcuts import get_object_or_404, render, redirect
from .models import Dispositivos
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
        registro = Acoes.objects.get(id=id)
    except:
        return redirect('listDevices')       
    
    if request.method == "POST":
        registro.nome = request.POST['nome']
        registro.endereco = request.POST['endereco']
        registro.save()

        return redirect('listDevices')
    
    return render(request, 'dispositivos/atualizar.html', {'registro': registro})