"""API encarregada de fazer a consulta dos dados do funcionario
    e retornar na tela FUNCIONARIOS esses dados."""

#Importando conexão com o banco de dados.
from api_conectDb import *
#Importando telas.
from api_iniTelas import *
#Importando função LIMPACAMPOS.
from api_limpaCampos import limp_cadfuncionarios

#Função encarregada de fazer a consulta dos dados do funionario dentro do DataBase.
def consul_funcionarios():
    
    id=principal.ent_id_fun.text() #Importando valores do campo ID dentro da tela FUNCIONARIOS.
    
    #Comandos a serem executados dentro do DataBase.
    cursor=con.cursor() #Criando a conexão com o DataBase.
    if id=="":
       #MessageBox informando que o ID digitado não foi encontrado.
       messagebox.showerror(title="Funcionario não encontrado", message="ID informado não foi encontrado")
    
    else:
        editdb=("SELECT * FROM tb_funcionario WHERE id='{}'".format(id)) #Comando a ser executado dentro do DataBase.
        cursor.execute(editdb) #Executando comando acima dentro do DataBase.
        dadosfun=cursor.fetchall() #Selecionando todos os dados demonstrados no DataBase a partir do comando editdb.
        cursor.close() #Fechando a conexão com o DataBase.

        #Setando dados coletados dentro da tela FUNCIONARIOS.
        principal.ent_nome_fun.setText(str(dadosfun[0][1])) #Setando o campo NOME do importando do DataBase na tela FUNCIONARIOS.
        principal.ent_cargo_fun.setText(str(dadosfun[0][2])) #Setando o campo CARGO do importando do DataBase na tela FUNCIONARIOS.
        principal.ent_nascimento_fun.setText(str(dadosfun[0][3])) #Setando o campo NASCIMENTO do importando do DataBase na tela FUNCIONARIOS.
        principal.ent_cpf_fun.setText(str(dadosfun[0][4])) #Setando o campo CPF do importando do DataBase na tela FUNCIONARIOS.
        principal.ent_contato_fun.setText(str(dadosfun[0][5])) #Setando o campo CONTATO do importando do DataBase na tela FUNCIONARIOS.
        principal.ent_email_fun.setText(str(dadosfun[0][6])) #Setando o campo EMAIL do importando do DataBase na tela FUNCIONARIOS.
        principal.ent_endereco_fun.setText(str(dadosfun[0][7])) #Setando o campo ENDEREÇO do importando do DataBase na tela FUNCIONARIOS.

