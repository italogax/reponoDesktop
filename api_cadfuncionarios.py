"""API encarregada de fazer o cadastro de novos FUNCIONARIOS no DataBase."""
#Importando conexão com o banco de dados.
from api_conectDb import *
#Importando telas.
from api_iniTelas import *
#Importando função LIMPACAMPOS.
from api_limpaCampos import limp_cadfuncionarios


#Função encarregada de fazer o cadastro de novos funcionarios no DataBase.
def cad_funcionarios():
        
        nome=principal.ent_nome_fun.text() #Importando valores do campo NOME da tela FUNCIONARIOS.
        cargo=principal.ent_cargo_fun.text() #Importando valores do campo CARGO da tela FUNCIONARIOS.
        nascimento=principal.ent_nascimento_fun.text() #Importando valores do campo NASCIMENTO da tela FUNCIONARIOS.
        cpf=principal.ent_cpf_fun.text() #Importando valores do campo CPF da tela FUNCIONARIOS.
        contato=principal.ent_contato_fun.text() #Importando valores do campo CONTATO da tela FUNCIONARIOS.
        email=principal.ent_email_fun.text() #Importando valores do campo EMAIL da tela FUNCIONARIOS.
        endereco=principal.ent_endereco_fun.text() #Importando valores do campo ENDERÇO da tela FUNCIONARIOS.

        #Comandos a serem executados dentro do DataBase.
        cursor=con.cursor() #Criando conexão com o DataBase.
        #Comando a ser executado dentro do DataBase para inserir dados de novos funcionarios no DataBase.
        editdb=("INSERT INTO tb_funcionario(id, nome, cargo, dt_nascimento, cpf, telefone, email, endereco) VALUES (null,%s,%s,%s,%s,%s,%s,%s)")
        editdb2=(nome, cargo, nascimento, cpf, contato, email, endereco) #Segunda parte do codigo acima.
        cursor.execute(editdb,editdb2) #Executando comandos acima no DataBase.
        con.commit() #Commitando comando executado no DataBase.
        cursor.close() #Fechando a conexão com o DataBase.

        limp_cadfuncionarios() #Executando função encarregada de fazer a limpeza dos campos da tela FUNCIONARIOS.
