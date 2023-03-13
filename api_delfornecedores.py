"""API encarregada de DELETAR dados de fornecedores dentro do DataBase."""

#Importando API encarregada de fazer a inicialização das telas.
from api_iniTelas import *
#Importando API encarregada de fazer a conexão com o DataBase.
from api_conectDb import *
#Importando API encarregada de fazer a limpeza dos campos da tela de FORNECEDORES.
from api_limpaCampos import limp_cadfornecedores

#Função encarregada de DELETAR dados de fornecedores dentro do DataBase.
def remo_fornecedores():
    id=principal.ent_id_for.text() #Importando valores do campo ID na tela FORNECEDORES.

    #Comandos a serem executados dentro do DataBase.
    cursor=con.cursor() #Criando a conexão com o DataBase.
    editdb=("DELETE FROM tb_fornecedores WHERE id='{}'".format(id)) #Comando a ser executado dentro do DataBase para remover dados de fornecedores.
    cursor.execute(editdb) #Executando comando dentro do DataBase.
    con.commit() #Commitando comando acima executado dentro do DataBase
    cursor.close() #Fechando a conexão com o dataBase.

    limp_cadfornecedores() #Executando função encarregada de fazer a limpeza dos campos da tela FORNECEDORES.

