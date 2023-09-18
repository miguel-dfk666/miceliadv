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
    if request.method == 'POST':
        selected_option = request.POST.get('opcao')
        
        if selected_option == 'numero_processo':
            return redirect('dashboard-numero-processo')
        elif selected_option == 'data_abertura':
            return redirect('dashboard-data-criacao')
        elif selected_option == 'numero_oab':
            return redirect('dashboard-numero-oab')

    return render(request, 'home.html')


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
            # Verifique se já existe um Processo com o mesmo numero_processo
            existing_processo = Processo.objects.filter(numero_processo=numero_processo).first()

            if existing_processo:
                # Lidar com o caso em que um registro com o mesmo numero_processo já existe
                messages.warning(request, f'Registro com numero_processo {numero_processo} já existe. Ignorando.')
            else:
                # Criar uma nova instância de Processo
                try:
                    processo = Processo(numero_processo=numero_processo)

                    # Preencha todos os campos do processo conforme necessário
                    processo.data_cadastro = data[0]
                    numero_dossie = data[1]
                    processo.coligada = data[2]
                    processo.agencia_departamento = data[3]
                    processo.area = data[4]
                    processo.tipo_de_acao = data[5]
                    processo.objeto_padrao = data[6]
                    processo.fase = data[7]
                    processo.inserido_por = data[8]
                    processo.alterado_por = data[9]
                    processo.data_de_alteracao = data[10]
                    processo.palavra_chave = data[11]
                    processo.valor_estimado = decimal.Decimal(data[12])
                    processo.valor_contingencia = decimal.Decimal(data[13])
                    processo.valor_causa = decimal.Decimal(data[14])
                    processo.valor_pedido = decimal.Decimal(data[15])
                    processo.valor_risco_possivel = decimal.Decimal(data[16])
                    processo.valor_risco_provavel = decimal.Decimal(data[17])
                    processo.risco_provavel_s_atu = data[18]
                    processo.valor_contingencia_civel = decimal.Decimal(data[19])
                    processo.data_estimada_prevista = data[20]
                    processo.data_estimada_pagamento = data[21]
                    processo.valor_risco = decimal.Decimal(data[22])
                    processo.risco = data[23]
                    processo.total_pago = decimal.Decimal(data[24])
                    processo.inss_empresa = decimal.Decimal(data[25])
                    processo.honorarios = decimal.Decimal(data[26])
                    processo.custas_processuais = decimal.Decimal(data[27])
                    processo.situacao = data[28]
                    processo.nome_desdobramento = data[29]
                    processo.data_ajuizamento = data[30]
                    processo.ult_desdobramento = data[31]
                    processo.instancia = data[32]
                    processo.rito = data[33]
                    processo.juizo = data[34]
                    processo.orgao = data[35]
                    processo.comarca = data[36]
                    processo.uf = data[37]
                    processo.numero_processo = data[38]
                    processo.cliente = data[39]
                    processo.cond_cliente = data[40]
                    processo.parte_adversa = data[41]
                    processo.cond_adversa = data[42]
                    processo.cpf_cnpj_adversa = data[43]
                    processo.autor_contumaz = data[44]
                    processo.motivo_desligamento = data[45]
                    processo.cargo = data[46]
                    processo.terceiro_interessado = data[47]
                    processo.terceiro = data[48]
                    processo.terceiro_prestador = data[49]
                    processo.cpf_cnpj_terceiro_prestador = data[50]
                    processo.advogado_credenciado = data[51]
                    processo.adv_adverso = data[52]
                    processo.adv_agressor = data[53]
                    processo.handle_perito = data[54]
                    processo.perito = data[55]
                    processo.data_encerramento = data[56]
                    processo.motivo_encerramento = data[57]
                    processo.exito = data[58]
                    processo.id_benner = data[59]
                    processo.data_evento = data[60]
                    processo.evento = data[61]
                    processo.tarefas = data[62]
                    processo.adv_centralizador = data[63]
                    processo.valor_risco_remoto = decimal.Decimal(data[64])
                    processo.observacao = data[65]
                    processo.data_atualizada = data[66]
                    processo.alterado_por_auditor = data[67]
                    processo.data_alteracao_auditor = data[68]
                    processo.danos = data[69]
                    processo.assunto = data[70]
                    processo.responsabilidade = data[71]
                    processo.causas_especiais = data[72]
                    processo.solic_enc_em = data[73]
                    processo.pendencias = data[74]
                    processo.inserido_por_evento = data[75]
                    processo.perc_controlador = data[76]
                    processo.perc_ex_controlador = data[77]
                    processo.revisao = data[78]
                    processo.solic_enc_por = data[79]
                    processo.tipo_desligamento = data[80]
                    processo.advogado_colaborador = data[81]
                    processo.equipe = data[82]
                    processo.data_do_fato = data[83]
                    processo.data_de_alteracao_da_fase = data[84]
                    processo.subarea = data[85]
                    processo.encerrado_em = data[86]
                    processo.encerrado_por = data[87]
                    processo.valor_acordo = decimal.Decimal(data[88])
                    processo.rede = data[89]
                    processo.regional = data[90]
                    processo.canal_de_contratacao = data[91]
                    processo.valor_condenacao_atual = decimal.Decimal(data[92])
                    processo.valor_encerramento = decimal.Decimal(data[93])
                    processo.valor_contabil_geral = decimal.Decimal(data[94])
                    processo.diferenca_encerramento = decimal.Decimal(data[95])
                    processo.porcentagem_diferenca_enc = data[96]
                    processo.indice_atualizacao = data[97]

                    processo.save()
                except decimal.InvalidOperation:
                    # Lidar com o caso em que os dados não são um número decimal válido
                    messages.warning(request, 'Valor decimal inválido detectado. Registro ignorado.')

        # Após o processamento bem-sucedido, redirecione o usuário para uma página de sucesso
        return HttpResponse('Dados importados com sucesso!')

    # Se o método HTTP não for POST, renderize a página de importação
    return render(request, 'importar_excel.html')


def dashboard_numero_processo(request):
    processos = Processo.objects.all()  
    return render(request, 'dashboard_numero_processo.html', {'processos': processos})

def dashboard_numero_oab(request):
    processos = Processo.objects.advogado_adverso_numero_oab() 
    return render(request, 'dashboard_numero_oab.html', {'processos': processos})

def dashboard_data_criacao(request):
    processos = Processo.objects.data_cadastro() 
    return render(request, 'dashboard_data_criacao.html', {'processos': processos})

