"""API encarregada de deletar os cadastros de CLIENTES no DataBase."""

#Importando API encarregada de fazer a inicialização das telas.
from api_iniTelas import *
#Importando API encarregada de fazer a conexão com o DataBase.
from api_conectDb import *
#Importando API encarregada de fazer a limpeza dos campos da tela CADASTRO DE CLIENTES.
from api_limpaCampos import limp_cadclientes

#Função encarregada de remover cadastro de clinetes no DataBase.
def remo_clientes(): 
    
    id=principal.ent_id_cli.text() #Importando valores do campo ID na tela de CLIENTES.
    
    cursor=con.cursor() #Criando uma conexão com o DataBase.
    editdb=("DELETE from tb_clientes WHERE id='{}'".format(id)) #Comando a ser executado dentro do DataBase para remover cadatro de CLIENTES.
    cursor.execute(editdb) #Executando o comando acima dentro do DataBase.
    con.commit() #Efetuando o commit da alteração dentro do DataBase.
    cursor.close() #Fechando a conexão com o DataBase.

    limp_cadclientes() #Executando função que faz a limpeza dos campos dentro da tela CLIENTES.