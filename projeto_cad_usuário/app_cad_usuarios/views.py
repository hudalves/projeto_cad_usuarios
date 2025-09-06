from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Usuario

def home (request):

    return render(request,'usuarios/home.html')
def listar(request):
    usuarios={
        'usuarios': Usuario.objects.all()
    }
    return render(request,'usuarios/usuarios.html',usuarios)
 
def usuarios(request):
    if request.method == 'POST':
        acao = request.POST.get('acao')
        # salavr os dados no banco
        if acao == 'enviar':
            
            novo_usuario = Usuario()
            novo_usuario.nome = request.POST.get('nome')
            novo_usuario.idade = request.POST.get('idade')
            usuarios = {'usuarios': Usuario.objects.all()}
            if not novo_usuario.nome or not novo_usuario.idade:
                messages.error(request, "Preencha todos os campos!")
            else:
                Usuario.objects.create(nome=novo_usuario.nome, idade=novo_usuario.idade)
                messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('home')
        elif acao == 'listar':
             return redirect('listagem_usuarios')
    usuarios={
        'usuarios': Usuario.objects.all()
    }
    
    # retorna os usuarios

    return render(request,'usuarios/usuarios.html',usuarios)
def excluir (request, id):
        usuario = get_object_or_404(Usuario, id_usuario=id)
        usuario.delete()
        return redirect('listagem_usuarios')
def editar(request, id):
     usuario = get_object_or_404(Usuario, id_usuario=id)
     if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
     if not nome or not idade:
        pass
     else:
        usuario.nome = nome
        usuario.idade = idade
        usuario.save()
        messages.success(request, "Usuário atualizado com sucesso!")
        return redirect('listagem_usuarios')
     
     return render(request, 'usuarios/editar.html', {'usuario': usuario})

