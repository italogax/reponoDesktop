"""APi encarregada de fazer o cadastro de FORNECEDORES."""

#Importando API encarregada de fazer a inicialização das telas.
from api_iniTelas import *
#Importando API encarregada de fazer a conexão com o DataBase.
from api_conectDb import *
#Importando API encarregada de fazer a limpeza dos campos da tela de FORNECEDORES.
from api_limpaCampos import limp_cadfornecedores

#Função encarregada de fazer a alteração de dados já exsitentes dentro do DataBase.
def alter_fornecedores(): 

    id=principal.ent_id_for.text() #Importando campo ** da tela FORNECEDORES.
    nome=principal.ent_nome_for.text() #Importando campo ** da tela FORNECEDORES.
    email=principal.ent_email_for.text() #Importando campo ** da tela FORNECEDORESES.
    telefone=principal.ent_telefone_for.text() #Importando campo ** da tela FORNECEDORES.
    cnpj=principal.ent_cnpj_for.text() #Importando campo ** da tela FORNECEDORES.

    #Função para fazer a verificação dos campos e detectar ce algum esta fazio
    if id == ''or nome == ''or email == ''or telefone == ''or cnpj == '':
        messagebox.showerror(title="Campo Vazio", message="Alteração interronpida, por favor preencha tds os campos!") #MessageBox informando que algum campo esta vazio.
    
    else:
        #Comando a serem executados dentro do DataBase.
        cursor=con.cursor() #Criando a conexão com o DataBase.
        #Comando a ser executado dentro do DataBase para alterar dados de FORNECEDORES já existentes dentro da TABLE.
        editdb=("UPDATE tb_fornecedores SET nome='{}', email='{}', telefone='{}', cnpj='{}' WHERE id='{}'".format(nome, email, telefone, cnpj, id))
        cursor.execute(editdb) #Executando comando dentro do DataBase.
        con.commit() #Commitando comando executado acima dentro do DataBase.
        cursor.close() #Fechando a conexão com o DataBase. 

        limp_cadfornecedores() #Executando função encarregada de fazer a limpeza dos campos da tela FORNECEDORES.