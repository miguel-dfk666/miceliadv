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

        if not new_processo.name.endswith('.xlsx'):
            messages.info(request, 'Formato de arquivo inválido')
            return render(request, 'importar_excel.html')

        imported_data = dataset.load(new_processo.read(), format='xlsx')
        for data in imported_data:
            try:
                # Verifique se já existe um Processo com o mesmo numero_processo
                numero_processo = data[41]
                existing_processo = Processo.objects.filter(numero_processo=numero_processo).first()

                if existing_processo:
                    # Lidar com o caso em que um registro com o mesmo numero_processo já existe
                    messages.warning(request, f'Registro com numero_processo {numero_processo} já existe. Ignorando.')
                else:
                    # Criar uma nova instância de Processo
                    processo = Processo(numero_processo=numero_processo)
                    # Preencha todos os campos do processo conforme necessário
                    processo.data_cadastro = data[0]
                    processo.numero_dossie = data[1]
                    processo.pasta_antiga = data[2]
                    processo.natureza = data[3]
                    processo.empresa_origem = data[4]
                    processo.coligada = data[5]
                    processo.agencia_departamento = data[6]
                    processo.area = data[7]
                    processo.tipo_de_acao = data[8]
                    processo.objeto_padrao = data[9]
                    processo.fase = data[10]
                    processo.inserido_por = data[11]
                    processo.alterado_por = data[12]
                    processo.data_de_alteracao = data[13]
                    processo.palavra_chave = data[14]
                    processo.valor_estimado = data[15]
                    processo.valor_contingencia = data[16]
                    processo.valor_causa = data[17]
                    processo.valor_pedido = data[18]
                    processo.valor_risco_possivel = data[19]
                    processo.valor_risco_provavel = data[20]
                    processo.risco_provavel_s_atu = data[21]
                    processo.valor_contingencia_civel = data[22]
                    processo.data_estimada_prevista = data[23]
                    processo.data_estimada_pagamento = data[24]
                    processo.valor_risco = data[25]
                    processo.risco = data[26]
                    processo.total_pago = data[27]
                    processo.inss_empresa = data[28]
                    processo.honorarios = data[29]
                    processo.custas_processuais = data[30]
                    processo.situacao = data[31]
                    processo.nome_desdobramento = data[32]
                    processo.data_ajuizamento = data[33]
                    processo.ult_desdobramento = data[34]
                    processo.instancia = data[35]
                    processo.rito = data[36]
                    processo.juizo = data[37]
                    processo.orgao = data[38]
                    processo.comarca = data[39]
                    processo.uf = data[40]
                    processo.cliente = data[42]
                    processo.cond_cliente = data[43]
                    processo.parte_adversa = data[44]
                    processo.cond_adversa = data[45]
                    processo.cpf_cnpj_adversa = data[46]
                    processo.autor_contumaz = data[47]
                    processo.motivo_desligamento = data[48]
                    processo.cargo = data[49]
                    processo.terceiro_interessado = data[50]
                    processo.terceiro = data[51]
                    processo.terceiro_prestador = data[52]
                    processo.cpf_cnpj_terceiro_prestador = data[53]
                    processo.advogado_credenciado = data[54]
                    processo.adv_adverso = data[55]
                    processo.adv_agressor = data[56]
                    processo.handle_perito = data[57]
                    processo.perito = data[58]
                    processo.data_encerramento = data[59]
                    processo.motivo_encerramento = data[60]
                    processo.exito = data[61]
                    processo.id_benner = data[62]
                    processo.data_evento = data[63]
                    processo.evento = data[64]
                    processo.tarefas = data[65]
                    processo.adv_centralizador = data[65]
                    processo.valor_risco_remoto = data[67]
                    processo.observacao = data[68]
                    processo.data_atualizada = data[69]
                    processo.alterado_por_auditor = data[70]
                    processo.data_alteracao_auditor = data[71]
                    processo.danos = data[72]
                    processo.assunto = data[73]
                    processo.responsabilidade = data[74]
                    processo.causas_especiais = data[75]
                    processo.solic_enc_em = data[76]
                    processo.pendencias = data[77]
                    processo.inserido_por_evento = data[78]
                    processo.perc_controlador = data[79]
                    processo.perc_ex_controlador = data[80]
                    processo.revisao = data[81]
                    processo.solic_enc_por = data[82]
                    processo.tipo_desligamento = data[83]
                    processo.advogado_colaborador = data[84]
                    processo.equipe = data[85]
                    processo.data_do_fato = data[86]
                    processo.data_de_alteracao_da_fase = data[87]
                    processo.subarea = data[88]
                    processo.encerrado_em = data[89]
                    processo.encerrado_por = data[90]
                    processo.valor_acordo = data[91]
                    processo.rede = data[92]
                    processo.regional = data[93]
                    processo.canal_de_contratacao = data[94]
                    processo.valor_condenacao_atual = data[95]
                    processo.valor_encerramento = data[96]
                    processo.valor_contabil_geral = data[97]
                    processo.diferenca_encerramento = data[98]
                    processo.porcentagem_diferenca_enc = data[99]
                    processo.indice_atualizacao = data[100]
                    processo.save()
            except Exception as e:
                # Lidar com o caso em que os dados não são um número decimal válido
                messages.warning(request, e)

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

