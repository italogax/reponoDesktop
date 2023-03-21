"""API encarregada de fazer uma consulta dentro do DataBase e rotarnar dados de CLIENTES."""

#Importando API encarregada de fazer a inicialização das telas.
from api_iniTelas import *
#Importando API encarregada de fazer a conexão com o DataBase.
from api_conectDb import *
#Importando API encarregada de limpar os campos da tela de CLIENTES
from api_limpaCampos import limp_cadclientes

#Função encarregada de SETAR os dados do DataBase na tela de CLIENTES.
def  set_clientes():
    id=principal.ent_id_cli.text() #Importando valores inseridos pelo user no campo ID. 
    cursor=con.cursor() #Cirando a conexão com o DataBase.
    editdb=("SELECT * FROM tb_clientes WHERE id='{}'".format(id)) #comando a ser executada dentro do DataBase fazer a seleção de todos os dados do CLIENTE.
    cursor.execute(editdb) #Executando função dentro do DataBase.
    dadoscli=cursor.fetchall() #Selecionando todos os dados demonstrados no DataBase a partir do comando do editdb.
    cursor=cursor.close() #Fechando a conexão com o DataBase.

    #Setando dados nos campos da tela CLIENTES.
    principal.ent_nome_cli.setText(str(dadoscli[0][1])) #Setando NOME do cliente.
    principal.ent_email_cli.setText(str(dadoscli[0][2])) #Setando EMAIL do cliente.
    principal.ent_contato_cli.setText(str(dadoscli[0][3])) #Setando TELEFONE do cliente.
    principal.ent_nascimento_cli.setText(str(dadoscli[0][4])) #Setando NASCIMENTO do cliente.
    principal.ent_cpf_cli.setText(str(dadoscli[0][5])) #Setando CPF do cliente.

#Função encarregada de fazer a consulta dos dados do cliente dentro do DataBase e retornar nos campoos da tela.
def verifi_clientes():

    id=int(principal.ent_id_cli.text()) #Importando valores inseridos pelo user no campo ID.

    cursor=con.cursor() #Cirando a conexão com o DataBase.
    editdb=("SELECT * FROM tb_clientes WHERE id='{}'".format(id)) #comando a ser executada dentro do DataBase fazer a seleção de todos os dados do CLIENTE.
    cursor.execute(editdb) #Executando função dentro do DataBase.
    
#=========================== VERIFICAÇÃO DE DADOS ===========================================================
    VerifCliente=cursor.fetchone() #Selecionando dados dentro do DataBase.
    try:
        #Fazendo a comparação dos dados.
        if(id in VerifCliente):
            set_clientes() #Executando função encarregada de fazer a inserção de dados dos clientes na tela CLIENTES.

    except:
        #MesssageBox que informa queo cliente não foi encontrado.
        messagebox.showerror(title="Erro", message="Cliente não encontrado!") 

        limp_cadclientes() #Executando função encarregada de limpar os campos da tela CLIENTES.
