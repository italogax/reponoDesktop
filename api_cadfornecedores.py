"""APi encarregada de fazer o cadastro de FORNECEDORES."""

#Importando API encarregada de fazer a inicialização das telas.
from api_iniTelas import *
#Importando API encarregada de fazer a conexão com o DataBase.
from api_conectDb import *
#Importando API encarregada de fazer a limpeza dos campos da tela de FORNECEDORES.
from api_limpaCampos import limp_cadfornecedores

#Função encarregada de fazer o cadastro de dados de novos fornecedores.
def cad_fornecedores():

    id=principal.ent_id_for.text() #Importando valores do campo ID na tela FORNECEDORES.
    nome=principal.ent_nome_for.text() #Importando valores do campo NOME na tela FORNECEDORES.
    email=principal.ent_email_for.text() #Importando valores do campo EMAIL na tela FONECEDORES.
    telefone=principal.ent_telefone_for.text() #Importando valores do campo TELEFONE na tela FONECEDORES.
    cnpj=principal.ent_cnpj_for.text() #Importando valores do campo CNPJ na tela FORNECEDORES.

    #Comandos executados dentro do DataBase.
    cursor=con.cursor() #Criando a conexão com o DataBase.
    editdb=("INSERT INTO tb_fornecedores (id, nome, email, telefone, cnpj) values(null,%s,%s,%s,%s)")
    campos=(nome, email, telefone, cnpj) #Agrupando dados importandos da tela FORNECEDORES.
    cursor.execute(editdb,campos) #Executando comando dentro do DataBase.
    con.commit() #Commitando alterações dentro do DataBase.
    cursor.close() #Fechando conexão com o DataBase.

    limp_cadfornecedores() #Executando função encarregada de fazer a limpeza dos campos da tela FORNECEDORES.
    