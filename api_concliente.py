"""API encarregada de fazer uma consulta dentro do DataBase e rotarnar dados de CLIENTES."""

#Importando API encarregada de fazer a inicialização das telas.
from api_iniTelas import *
#Importando API encarregada de fazer a conexão com o DataBase.
from api_conectDb import *
#Importando API encarregada de limpar os campos da tela de CLIENTES
from api_limpaCampos import limp_cadclientes

#Função encarregada de fazer a consulta dos dados do cliente dentro do DataBase e retornar nos campoos da tela.
def consul_clientes():

    id=principal.ent_id_cli.text() #Importando valores inseridos pelo user no campo ID.

    cursor=con.cursor() #Criando a conexão com o DataBase.
    #Caso o campo ID esteja vazio.
    if id== "":
        #MessageBox informando que o ID não foi encotrado.
        messagebox.showerror(title="Cliente não encotrado", 
        message="""ID do cliente não foi encotrado!
        Verifique na tabela de clientes se o ID esta correto.""")

        limp_cadclientes() #Executando função encarregada de fazer a limpeza dos campos da tela CLIENTES.

    else:
        editdb=("SELECT * FROM tb_clientes WHERE id='{}'".format(id)) #comando a ser executada dentro do DataBase fazer a seleção de todos os dados do CLIENTE.
        cursor.execute(editdb) #Executando função dentro do DataBase.
        dadoscli=cursor.fetchall() #Selecionando todos os dados demonstrados no DataBase a partir do comando do editdb.
        cursor=cursor.close() #Fechando a conexão com o DataBase.

        #Setando dados nos campos da tela CLIENTES.
        principal.ent_nome_cli.setText(str(dadoscli[0][1])) #Setando NOME do cliente.
        principal.ent_email_cli.setText(str(dadoscli[0][2])) #Setando EMAIL do cliente.
        principal.ent_contato_cli.setText(str(dadoscli[0][3])) #Setando TELEFONE do cliente.
        principal.ent_cpf_cli.setText(str(dadoscli[0][4])) #Setando CPF do cliente.

        