"""API encarregada de fazer o cadastro de CLIENTES dentro do DataBase."""

#Importando API encarregada de fazer a inicialização das telas.
from api_iniTelas import *
#Importando API encarregada de fazer a conexão com o DataBase.
from api_conectDb import *
#Importando API encarregada de fazer a limpeza dos campos da tela CADASTRO DE CLIENTES.
from api_limpaCampos import limp_cadclientes

#Função encarregada de fazer o cadastro dos dados cliente.
def cad_cliente(): 

    nome=principal.ent_nome_cli.text() #Importando os valores do campo NOME do cliente.
    email=principal.ent_email_cli.text() #Importano os valores do campo EMAIL do cliente.
    telefone=principal.ent_contato_cli.text() #Importando os valores do campo TELEFONE do cliente.
    cpf=principal.ent_cpf_cli.text() #Importando os valores do campo CPF do cliente.
    
    cursor=con.cursor() #Criando a conexão com o DataBase.
    comandodb=("INSERT INTO tb_clientes (id, nome, email, telefone, cpf) values(null,%s,%s,%s,%s)") #Comando encarregado de fazer o cadastro dos novos clientes.
    campos=( nome, email, telefone, cpf) #Capiturando os dados a serem inseridos na linha do novo cliente.
    cursor.execute(comandodb,campos) #Executando os comandos para inserir os novos clientes dentro do DataBase. 
    con.commit() #Comitando alterações dentro do DataBase.
    cursor.close() #Fechando conexão com o DataBase.

    limp_cadclientes() #Execuntando função encarregado de fazer a limpeza dos cmpos da tela CLIENTES.

    
