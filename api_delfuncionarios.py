"""API encarregada de fazer o DELETE de dados existentes no DataBase."""

#Importando conexão com o banco de dados.
from api_conectDb import *
#Importando telas.
from api_iniTelas import *
#Importando função LIMPACAMPOS.
from api_limpaCampos import limp_cadfuncionarios


#Função encarregada de fazer a remoção de dados do DataBase na TABLE de FUNCIONARIOS.
def remo_funcionarios():

    id=principal.ent_id_fun.text() #Importando valores do campo ID na tela FUNCIONARIOS.

    #Comandos a serem executados dentro do DataBase.
    cursor=con.cursor() #Criando a conexão no DataBase.
    editdb=("DELETE FROM tb_funcionario WHERE id='{}'".format(id))
    cursor.execute(editdb) #Executando comando acima dentro do DataBase.
    con.commit() #Commitando comando dentro do DataBase.
    cursor.close() #Fechando a conexão com o DataBase.

    limp_cadfuncionarios() #Executando função que faz a limpeza dos campos da tela FUNCIONARIOS. 
