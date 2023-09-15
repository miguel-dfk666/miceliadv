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

    todas_opcoes = processos  # Assuming you want to pass all Processo objects to the template

    return render(request, 'home.html', {'todas_opcoes': todas_opcoes})


def simple_upload(request):
    if request.method == 'POST':
        processo_resource = ProcessoResource()
        dataset = Dataset()
        new_processo = request.FILES['dados_planilha']

        if not new_processo.name.endswith('xlsx'):
            messages.info(request, 'Formato de arquivo inválido')
            return render(request, 'importar_excel.html')

        imported_data = dataset.load(new_processo.read(), format='xlsx')
        for data in imported_data:
            numero_processo = data[5]

            # Check if a Processo with the same numero_processo already exists
            existing_processo = Processo.objects.filter(numero_processo=numero_processo).first()

            if existing_processo:
                # Handle the case where a record with the same numero_processo exists
                messages.warning(request, f'Record with numero_processo {numero_processo} already exists. Skipping.')
            else:
                # Create a new Processo instance
                try:
                    valor_estimado = decimal.Decimal(data[1])
                    valor_causa = decimal.Decimal(data[2])
                    valor_pedido = decimal.Decimal(data[3])
                    valor_risco_provavel = decimal.Decimal(data[4])

                    processo = Processo(
                        numero_processo=numero_processo,
                        data_cadastro=data[0],
                        coligacao=data[10],
                        numero_dossie=data[9],
                        tipo_de_acao=data[11],
                        obj_padrao=data[12],
                        advogado_adverso=data[6],
                        advogado_agressor=data[7],
                        advogado_colaborador=data[8],
                        valor_estimado=valor_estimado,
                        valor_causa=valor_causa,
                        valor_pedido=valor_pedido,
                        valor_risco_provavel=valor_risco_provavel,
                    )
                    processo.save()
                except decimal.InvalidOperation:
                    # Handle the case where the data is not a valid decimal number
                    messages.warning(request, 'Invalid decimal value detected. Record skipped.')

        # After successful processing, redirect the user to a success page
        return HttpResponse('Dados importados com sucesso!')

    # If the HTTP method is not POST, render the import page
    return render(request, 'importar_excel.html')


def dashboard_numero_processo(request):
    processos = Processo.objects.all()  
    return render(request, 'dashboard_numero_processo.html', {'processos': processos})

def dashboard_numero_oab(request):
    processos = Processo.objects.all() 
    return render(request, 'dashboard_numero_oab.html', {'processos': processos})

def dashboard_data_criacao(request):
    processos = Processo.objects.all() 
    return render(request, 'dashboard_data_criacao.html', {'processos': processos})
