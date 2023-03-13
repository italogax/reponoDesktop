"""API encarregada de fazer a consulta de dados dentro do DataBase e reotrnar nos campos da tela FORNECEDORES."""

#Importando API encarregada de fazer a inicialização das telas.
from api_iniTelas import *
#Importando API encarregada de fazer a conexão com o DataBase.
from api_conectDb import *
#Importando API encarregada de fazer a limpeza dos campos da tela de FORNECEDORES.
from api_limpaCampos import limp_cadfornecedores


def con_fornecedores():

    id=principal.ent_id_for.text() #Importando valores do campo ID na tela de FORNECEDORES.

    #Comandos a serem executados no DataBase.
    cursor=con.cursor() #Criando a conexão com o DataBase.
    #Caso o campo ID esteja vazio.
    if id=="":
        #MessageBox informando que o ID não foi encontrado.
        messagebox.showerror(title="Erro de pesquisa.", 
        message="ID não encontrado no DataBase.")

        limp_cadfornecedores() #Executando função encarregada de fazer a limpeza de todos os campos da tela FORNECEDORES.

    else:
        editdb=("SELECT * FROM tb_fornecedores WHERE id='{}'".format(id)) #Comando a ser executado dentro do DataBase para retornar todos os campos de um forncedor.
        cursor.execute(editdb) #Executando comando dentro do DataBase.
        dadosfor=cursor.fetchall() #Selecionando todos os campos demosntrados na tabale apos executar o comando acima.

        #Setando dados nos campos da tela FORNECEDORES.
        principal.ent_nome_for.setText(str(dadosfor[0][1])) #Limpando o campo NOME na tela FORNECEDORES.
        principal.ent_email_for.setText(str(dadosfor[0][2])) #Limpando o campo EMAIL na tela FORNECEDORES.
        principal.ent_telefone_for.setText(str(dadosfor[0][3])) #Limpando o campo TELEFONE na tela FORNECEDORES.
        principal.ent_cnpj_for.setText(str(dadosfor[0][4])) #Limpando o campo CNPJ na tela FORNECEDORES.

