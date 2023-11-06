from django.shortcuts import render, redirect, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from .models import Processo
from .resources import ProcessoResource
from tablib import Dataset
import pandas as pd
import decimal

# register request


def HomePage(request):
    return render(request, 'core/home.html')


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
            return render(request, 'auth/login.html', {'error_message': 'Usuário e/ou senha incorretos.'})
    return render(request, 'auth/login.html')


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

    return render(request, 'auth/singup.html')


def logout_view(request):
    # Lógica de logout aqui
    return redirect('login')


def processar_opcao(request):
    if request.method == 'POST':
        selected_option = request.POST.get('opcao')
        
        if selected_option == 'numero_processo':
            return redirect('dashboard-numero-processo')
        elif selected_option == 'data_abertura':
            return redirect('dashboard-data-criacao')
        elif selected_option == 'numero_oab':
            return redirect('dashboard-numero-oab')

    return render(request, 'core/home.html')


def simple_upload(request):
    if request.method == 'POST':
        processo_resource = ProcessoResource()
        dataset = Dataset()
        new_processo = request.FILES['base_dados']

        if not new_processo.name.endswith('.xlsx'):
            messages.info(request, 'Formato de arquivo inválido')
            return render(request, 'core/importar_excel.html')

        imported_data = dataset.load(new_processo.read(), format='xlsx')
        for data in imported_data:
            try:
                # Verifique se já existe um Processo com o mesmo numero_processo
                numero_processo = data[5]
                existing_processo = Processo.objects.filter(numero_processo=numero_processo).first()

                if existing_processo:
                    # Lidar com o caso em que um registro com o mesmo numero_processo já existe
                    messages.warning(request, f'Registro com numero_processo {numero_processo} já existe. Ignorando.')
                else:
                    # Criar uma nova instância de Processo
                    processo = Processo(numero_processo=numero_processo)
                    # Preencha todos os campos do processo conforme necessário
                    processo.documento = data[0]
                    processo.julgo_procedente = data[1]
                    processo.julgo_improcedente = data[2]
                    processo.dano_moral = data[3]
                    processo.dano_material = data[4]
                    processo.status = data[6]
                    processo.advogado_oab = data[7]
                    processo.advogado_nome = data[8]
                    processo.assunto = data[9]
                    processo.foro = data[10]
                    processo.vara = data[11]
                    processo.juiz = data[12]
                    processo.distribuicao = data[13]
                    processo.numero_controle = data[14]
                    processo.area = data[15]
                    processo.valor_acao = data[16]
                    processo.outros_assuntos = data[17]
                    processo.patrono = data[18]
                    processo.reu = data[19]
                    processo.instituicao = data[20]
                
                    processo.save()
            except Exception as e:
                # Lidar com o caso em que os dados não são um número decimal válido
                messages.warning(request, e)

        # Após o processamento bem-sucedido, redirecione o usuário para uma página de sucesso
        return HttpResponse('Dados importados com sucesso!')

    # Se o método HTTP não for POST, renderize a página de importação
    return render(request, 'importar_excel.html')

