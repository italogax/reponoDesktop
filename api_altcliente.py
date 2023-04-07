"""API encarregada de fazer todas as alterçãoes nos dados do CLIENTE dentro do DataBase."""

#Importando API encarregada de fazer a inicialização das telas.
from api_iniTelas import *
#Importando API encarregada de fazer a conexão com o DataBase.
from api_conectDb import *
#Importando API encarregada de fazer a limpeza dos campos da tela de CLIENTES.
from api_limpaCampos import limp_cadclientes

#Função encarregada de fazer a alteração nos dados já existentes dentro do DataBase.
def alter_clientes():

    id=principal.ent_id_cli.text() #Importando os valores do campo ID do cliente.
    nome=principal.ent_nome_cli.text() #Importando os valores do campo NOME do cliente.
    email=principal.ent_email_cli.text() #Importano os valores do campo EMAIL do cliente.
    telefone=principal.ent_contato_cli.text() #Importando os valores do campo TELEFONE do cliente.
    nascimento=principal.ent_nascimento_cli.text() #Importando os valores do campo DATA NASCIMENTO do CLIENTES.
    cpf=principal.ent_cpf_cli.text() #Importando os valores do campo CPF do cliente.
    
    #Função para fazer a verificação dos campos e detectar ce algum esta fazio
    if id == '' or nome == '' or email == '' or telefone == '' or nascimento == '' or cpf == '':
        messagebox.showerror(title="Campo Vazio", message="Alteração interronpida, por favor preencha tds os campos!") #MessageBox informando que algum campo esta vazio.
    
    else:
        #Comando dentro do SQL
        cursor=con.cursor() #Conexão com o DataBase.
        #Comando executado dentro do DataBase para gerar a atualização nos dados.
        editdb=("UPDATE tb_clientes SET nome='{}',email='{}',telefone='{}',dt_nascimento='{}',cpf='{}' WHERE id='{}'".format(nome, email, telefone, nascimento, cpf, id))
        cursor.execute(editdb) #Executando comando dentro do DataBase.
        con.commit() #Commitando dados atualizados dentro do DataBase.
        cursor.close() #Fechando a conexão do DataBase.
        limp_cadclientes() #Limpando os campos da tela de CLIENTES.
    
