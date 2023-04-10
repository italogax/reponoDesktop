"""Está API é encarregada de efetuar as consultas no DataBase e retornar dados dos
    produtos tanto na tela de cadastrar dados quanto na tela de inventario onde temos uma tabela"""

#Importando conexão com o banco de dados.
from api_conectDb import *
#Importando telas.
from api_iniTelas import *
#Importando função LIMPACAMPOS.
from api_limpaCampos import *
#Função encarregada de gerar a mensagem de erro do ID.
def msg_erro():
    #MessageBox informando que o ID não foi encontrado.
    messagebox.showerror(title="Id não encontrado", message="""Por favor verficque na aba INVENTARIO o ID que procura!""")#Caso tenha digita algum ID no campo ID.

def pesquisa_id():
    id=principal.ent_id_pro.text() #Importando valores inseridos pelo user no campo ID.
    cursor=con.cursor() #Conexão no DataBase.
    editabanco=("SELECT * FROM tb_produtos WHERE id= '{}'".format(id)) #Comando que seleciona a coluna a partir do ID.
    cursor.execute(editabanco) #Executando o EDITABANCO dentro do DataBase.
    campos = cursor.fetchall() #Selecionando toda a linha com as colunas no DataBase.

    principal.ent_produto_pro.setText(str(campos[0][1])) #Setando a primeira coluna.
    principal.ent_categoria_pro.setText(str(campos[0][2])) #Setando a segunda coluna.
    principal.ent_fornecedor_pro.setText(str(campos[0][3])) #Setando a terceira coluna.
    principal.ent_quantidade_pro.setText(str(campos[0][6])) #Setando a quinta coluna.
    principal.ent_vlcompra_pro.setText(str(campos[0][4])) #Setando a terceira coluna.
    principal.ent_vlvenda_pro.setText(str(campos[0][5])) #Setando a quarta coluna.

#Função encarregada de fazer a consulta de PRODUTOS no DataBase retornar dados na tela.
def verifi_id_pro():

    id=int(principal.ent_id_pro.text()) #Importando valores inseridos pelo user no campo ID.
    
    cursor=con.cursor() #Criando conexão com o dataBase.
    editdb=("SELECT * FROM tb_produtos WHERE id='{}'".format(id)) #Comando a ser executado dentro do DataBase.
    cursor.execute(editdb) #Executando comando acima dentro do DataBase.
    
    #================== Verificação do ID do produto ====================================================================
    
    verifiProduto=cursor.fetchone() #Selecionando campo especifico no DataBase.
    try:
        #Fazendo a comparação de dados no DataBase.
        if(id in verifiProduto):
            pesquisa_id() #Execuntando função que seta os campos do DataBase na tela PRODUTOS.

    except:
        msg_erro() #Executando função encarregada de mostrar a mensagem de erro.
        limp_cadProdutos() #Executando função encarregada de fazer a limpeza dos campos da tela PRODUTOS.

#Função a ser executada apos clicar no botton INVENTARIO.
def consul_produtos():

    cursor=con.cursor() #Conexão com o DataBase.
    
    editabanco=("SELECT * from tb_produtos") #Comando que seleciona todas as linhas e todas as colunas no DataBase.
    cursor.execute(editabanco) #Executando comando EDITABANCO dentro do DataBase.
    campos=cursor.fetchall() #Selecionando todas as linhas, colunas do DataBase.
    principal.tab_inventario.setRowCount(len(campos)) #Definindo a contagem de linhas da table. 
    principal.tab_inventario.setColumnCount(7) #Definindo a contagem de colunas da table.
    for l in range(len(campos)): #Inserindo todas as linhas da DataBase na table.
        for c in range(0,7): #Inserindo todas as colunas do DataBase na table.
            principal.tab_inventario.setItem(l,c,QtWidgets.QTableWidgetItem(str(campos[l][c]))) #Setando os ITENS dentro da table.
    cursor.close() #Fechando a conexão com o DataBase.

#Função encarregada de verificar se o conteudo do ID é nulo.
def check_conteudo_pr():
    id=principal.ent_id_pro.text() #Importando conteudo do campo ID na tela PRODUTOS.
    
    #Se o campo ID for Vazio.
    if id == "":
        msg_erro()
    #Se o campo ID não for Vazio. 
    else:
        verifi_id_pro() #Executando função encarregada de verificar se o ID é exsitente no DataBase.

