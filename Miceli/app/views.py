from django.shortcuts import  render, redirect, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login 
from .models import Processo
from django.db.models import Sum
import pandas as pd

# register request
def HomePage(request):
  return render(request, 'home.html')

def Login(request):
	if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['pass']

			# Autentica o usuário
			user = authenticate(request, username=username, password=password)

			if user is not None:
			# Credenciais corretas, faça login e redirecione para a página home
				login(request, user)
				return redirect('home')
			else:
				# Credenciais incorretas, exibe um alert box
				return render(request, 'login.html', {'error_message': 'Usuário e/ou senha incorretos.'})
	return render(request, 'login.html')

def Register(request):
  if request.method == 'POST':
    uname = request.POST.get('username')
    email = request.POST.get('email')
    pass1 = request.POST.get('password1')
    pass2 = request.POST.get('password2')
    
     # Check if a user with the same username or email already exists
    if User.objects.filter(username=uname).exists() or User.objects.filter(email=email).exists():
      error_message = "O nome de usuário e/ou email já é existente, escolha um outro nome de usuário e/ou email"
      return redirect(f'/register/?error={error_message}')
    
    my_user = User.objects.create_user(uname, email, pass1)
    my_user.save()
    return redirect('/login/?success=Conta criada com sucesso!')

  return render(request, 'singup.html')


def logout_view(request):
    # Lógica de logout aqui
    return redirect('login')


def processar_opcao(request):
    processos = Processo.objects.all()

    if request.method == 'POST':
        opcao_selecionada = request.POST.get('opcao')
        # Realize as operações necessárias com a opção selecionada aqui
        # Em seguida, exiba os dashboards com as informações do banco de dados

    return render(request, 'home.html', {'todas_opcoes': todas_opcoes})


