"""API encarregada de fazer a alteração em dandos de FUNCIONARIOS já cadastrados."""

#Importando conexão com o banco de dados.
from api_conectDb import *
#Importando telas.
from api_iniTelas import *
#Importando função LIMPACAMPOS.
from api_limpaCampos import limp_cadfuncionarios

#Função encarregada de fazer ALTERAÇÕES nos dados de FUNCIONARIOS do DataBase.
def alter_funcionarios():

    id=principal.ent_id_fun.text() #Importando valores do campo ID da tela de FUNCIONARIOS.
    nome=principal.ent_nome_fun.text() #Importando valores do campo NOME da tela FUNCIONARIOS.
    cargo=principal.ent_cargo_fun.text() #Importando valores do campo CARGO da tela FUNCIONARIOS.
    nascimento=principal.ent_nascimento_fun.text() #Importando valores do campo NASCIMENTO da tela FUNCIONARIOS.
    cpf=principal.ent_cpf_fun.text() #Importando valores do campo CPF da tela FUNCIONARIOS.
    contato=principal.ent_contato_fun.text() #Importando valores do campo CONTATO da tela FUNCIONARIOS.
    email=principal.ent_email_fun.text() #Importando valores do campo EMAIL da tela FUNCIONARIOS.
    endereco=principal.ent_endereco_fun.text() #Importando valores do campo ENDERÇO da tela FUNCIONARIOS.

    #Função para fazer a verificação dos campos e detectar ce algum esta fazio
    if id == '' or nome == '' or cargo == '' or nascimento == '' or cpf == '' or contato == '' or email == '' or endereco == '':
        messagebox.showerror(title="Campo Vazio", message="Alteração interronpida, por favor preencha tds os campos!") #MessageBox informando que algum campo esta vazio.
    
    else:
        #Comandos a serem executados dentro do DataBase.
        cursor=con.cursor() #Criando a conexão com o DataBase.
        #Comando a ser executado dentro do DataBase para alterar os dados de FUNCIONARIOS.
        editdb=("UPDATE tb_funcionario SET nome='{}', cargo='{}', dt_nascimento='{}', cpf='{}', telefone='{}', email='{}', endereco='{}' WHERE id='{}'".format(nome,cargo,nascimento,cpf,contato,email,endereco, id))
        cursor.execute(editdb) #Executando comando acima para altera dados de FUNCIONARIOS.
        con.commit() #Commitando dados inseridos no DataBase.
        cursor.close() #Fechando a conexão no DataBase.

        limp_cadfuncionarios() #Executando função encarregada de fazer a limpeza dos campos da tela FUNCIONARIOS.