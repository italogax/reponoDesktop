"""API encarregada de fazer a consulta de dados dentro do DataBase e reotrnar nos campos da tela FORNECEDORES."""

#Importando API encarregada de fazer a inicialização das telas.
from api_iniTelas import *
#Importando API encarregada de fazer a conexão com o DataBase.
from api_conectDb import *
#Importando API encarregada de fazer a limpeza dos campos da tela de FORNECEDORES.
from api_limpaCampos import limp_cadfornecedores

#Função encarregada de gerar a mensagem de erro do ID.
def msg_erro():
    #MessageBox informando que o ID não foi encontrado.
    messagebox.showerror(title="Erro de pesquisa.", 
    message="ID não encontrado no DataBase.")

#Função encarregada de fazer a inserção de dados do funcionario na tela FUNCIONARIOS.
def set_fornecedores():
        
    id=principal.ent_id_for.text() #Importando valores do campo ID na tela de FORNECEDORES.

    cursor=con.cursor() #Criando a conexão com o DataBase.
    editdb=("SELECT * FROM tb_fornecedores WHERE id='{}'".format(id)) #Comando a ser executado dentro do DataBase para retornar todos os campos de um forncedor.
    cursor.execute(editdb) #Executando comando dentro do DataBase.
    dadosfor=cursor.fetchall() #Selecionando todos os campos demosntrados na tabale apos executar o comando acima.

    #Setando dados nos campos da tela FORNECEDORES.
    principal.ent_nome_for.setText(str(dadosfor[0][1])) #Limpando o campo NOME na tela FORNECEDORES.
    principal.ent_email_for.setText(str(dadosfor[0][2])) #Limpando o campo EMAIL na tela FORNECEDORES.
    principal.ent_telefone_for.setText(str(dadosfor[0][3])) #Limpando o campo TELEFONE na tela FORNECEDORES.
    principal.ent_cnpj_for.setText(str(dadosfor[0][4])) #Limpando o campo CNPJ na tela FORNECEDORES.


def con_fornecedores():

    id=int(principal.ent_id_for.text()) #Importando valores do campo ID na tela de FORNECEDORES.

    #Comandos a serem executados no DataBase.
    cursor=con.cursor() #Criando a conexão com o DataBase.
    editdb=("SELECT * FROM tb_fornecedores WHERE id='{}'".format(id)) #Comando a ser executado dentro do DataBase para retornar todos os campos de um forncedor.
    cursor.execute(editdb) #Executando comando dentro do DataBase.

#===================================== VERIFICAÇÃO DE DADOS DO FORNECEDOR ======================================================================================

    VeriFor=cursor.fetchone() #Selecionando dados dos fornecedores no DataBase.
    try:
        #Fazendo a comparação de dados do FORNECEDOR.
        if(id in VeriFor):
            set_fornecedores() #Executando função encarregada de fazer a inserção de dados na tela FORNECEDORES.
        
    except:
        msg_erro() #Executando função encarregada de gerar a mensagem de erro.
        limp_cadfornecedores() #Executando função encarregada de fazer a limpeza de todos os campos da tela FORNECEDORES.

    
    #Função encarregada de fazer a verificação se o campo ID é nulo.
def check_conteudo_fo():
    id=principal.ent_id_for.text() #Importando conteudo do campo ID na tela de FORNECEDORES.

    #Se o campo ID estiver Vazio.
    if id == "":
        msg_erro() #Executando função encarregada de gerar a mensagem de erro no ID.

    #Se o Campo ID não estiver Vazio.
    else: 
        con_fornecedores() #Excutando função que faz a verificação da existencia do ID no DataBase.
        
            