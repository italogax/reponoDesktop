"""API encarregada de fazer todo o funcionamento do PVD"""

from tkinter import messagebox
#Importando telas do System.
from api_iniTelas import *
#Importando conexão com o DataBase.
from api_conectDb import *
#Importando função que limpa os campos.
from api_limpaCampos import limp_caixa
#Importando bibliotecas para gerar o numero ALFANUMERICO.
import string
from random import choice

#Função encarregada de demonstrar os produtos da compra na tabela e nos campos.
def monstra_produtos():

    id=principal.ent_idcaixa.text() #Importando conteudo do campo ID inserido pelo USER.

    cursor=con.cursor() #Estabelecendo conexão com o DataBase.
    pesqprodutos=("SELECT * FROM tb_produtos WHERE id='{}'".format(id)) #Comando a ser executado dentro do DataBase.
    cursor.execute(pesqprodutos) #Executando comando PESQPRODUTOS.
    campos=cursor.fetchall() #Selecionando toda a linha selecionada no DataBase.

    #Campos da tela---------------------------------
    principal.ent_produtocaixa.setText(str(campos[0][1])) #Setando nome do produto.
    principal.ent_valorcaixa.setText(str(campos[0][5])) #Setando valor de venda.


#Função encarregada de fazer a verificação do ID no DataBase.
def verifi_id():

    id=int(principal.ent_idcaixa.text()) #Importando conteudo do campo ID inserido pelo USER.
    
    cursor=con.cursor() #Criando a conexão com o DataBase.
    editdb=("SELECT * FROM tb_produtos WHERE id='{}'".format(id)) #Comando a ser executado dentro do DataBase para verificar se o ID é existente.
    cursor.execute(editdb) #Executando comando acima dentro do DataBase.
    
#================== Verificação do ID do produto ====================================================================
    VerifiProduto=cursor.fetchone() #Selecionando todos os campos apresentados no DataBase.

    try:
        #Fazendo a comparação do ID apresetado pelo USER aos IDs contidos no DataBase.
        if(id in VerifiProduto):
            monstra_produtos() #Executando função que SETA os dados do DataBase nos campos da tela do CAIXA.
    
    except:
        #MensageBox de erro caso o ID não seja encontrado.
        messagebox.showerror(title="Erro", message="Codigo do produto incorreto!")
        limp_caixa() #Executando função encarregada de limpar os camposs da tela do CAIXA.

#Função encarregada de fazer o commit dos dados aputados na tela do CAIXA no DataBase.
def up_table():

    id=principal.ent_idcaixa.text() #Importando valores inseridos pelo user no campo ID.
    produto=principal.ent_produtocaixa.text() #Importando valores inseridos pelo SYSTEM no campo PRODUTO.
    valoruni=principal.ent_valorcaixa.text() #Importando valores inseridos pelo SYSTEM no campo VALOR UNITARIO.
    quantidade=principal.ent_qtcaixa.text() #Importando valores inseridos pelo USER no campo QUANTIDADE.
    
    valoruni = float(valoruni) #Transformando variavel STR em FLOAT.
    quantidade = int(quantidade) #Transformando variavel STR em FLOAT.
    vl_total= valoruni * quantidade #Multiplicação para fazer o calculo do valor total daquele produto. 
    #vl_total= str(vl_total)

    cursor=con.cursor() #Estabelecendo conexão com o banco de dados.
    edittb=("INSERT INTO tb_vendarotativa(id, produto, quantidade, vl_unidade, vl_total) values (%s,%s,%s,%s,%s)") #Comando a ser executado dentro do DataBase.
    edittb2=(id,produto,quantidade,valoruni, vl_total) #Dados importados da tela para serem inseridos no DataBase.
    cursor.execute(edittb,edittb2) #Executando comandos detro do DataBase.
    con.commit() #Comitando os comandos dentro do DataBase.
    cursor.close() #Fechando conexão com o DataBase.

#Função encarregada de mostrar os 
def set_tablepvd():

    cursor=con.cursor() #Fazendo a conexão com o DataBase.
    edittb=("SELECT * FROM tb_vendarotativa") #Comando para selecionar todos os campos da tabela.
    cursor.execute(edittb) #Executando comando dentro do DataBase.
    campos=cursor.fetchall() #Comando para selecionar todos os campos do DataBase.
    principal.tab_caixa.setRowCount(len(campos)) #Setando a quantidade de linhas que tem dentro do DataBase.
    principal.tab_caixa.setColumnCount(6) #Setando a quantidade de colunas que a tabela tem.
    
    for l in range(len(campos)): #Inserindo todas as linhas da DataBase na table.nse 
        for c in range(0,6):#Inserindo todas as colunas do DataBase na table.
            principal.tab_caixa.setItem(l,c,QtWidgets.QTableWidgetItem(str(campos[l][c]))) #Setando os ITENS dentro da table.
    cursor.close() #Fechando a conexão com o DataBase.

#Função encarregada de preencher o subtotal    
def sub_total():
    quantidade=principal.ent_qtcaixa.text() #Importando valores do campo QUANTIDADE inserido pelo user.
    subtotal=principal.ent_subtotalcaixa.text() #Importando valores do campo SUBTOTAL da tela do caixa.
    valoruni=principal.ent_valorcaixa.text()
    if quantidade=="":
        principal.ent_qtcaixa.setText("1")
        sub_total()
    else:
        valoruni= float(valoruni) #Convertendo variavel STR para FLOAT.
        quantidade= int(quantidade)  #Convertendo variavel STR para INT.
        
        calq_vl= quantidade * valoruni #Calculo para chegar ao valor do subprodutos.

        #Caso valor do SUBTOTAL seja NULO.
        if subtotal =="": 
            calq_vl = str(calq_vl) #Convertendo variaveis FLOAT em STR.
            subtotal=principal.ent_subtotalcaixa.setText(calq_vl) #Setando valor do subtotal.
            up_table() #Chamando função que faz a inserção dos dados dentro do DataBase.
            set_tablepvd() #Chamando função que intruduz os dados na tabela do CAIXA.
            limp_caixa() #Função encarregada de limpar os campos preenchidos pelo USER.

        #Caso valor do SUBTOTAL nao senha NULO.
        else:
            subtotal= float(subtotal) #Convertendo variavel STR em FLOAT.
            calq_vl=(calq_vl + subtotal) #Calculo para chegar ao valor do subtotal.
            calq_vl= str(calq_vl) #COnvertendo variavel FLOAT em STR.
            subtotal=principal.ent_subtotalcaixa.setText(calq_vl) #Setando valor do sub total. 
            up_table() #Chamando função que faz a inserção dos dados dentro do DataBase.
            set_tablepvd() #Chamando função que intruduz os dados na tabela do CAIXA.
            limp_caixa()

#Função encarregada de fazer a limpeza da TAB_VENDAROTATIVA.
def limpa_tabrotativa():

    cursor=con.cursor() #Conexão do DataBase.
    editlimp=("TRUNCATE tb_vendarotativa;") #Comando a ser executado dentro do DataBase.
    cursor.execute(editlimp) #Executando comando dentro do DataBase.
    cursor.close() #Fechando conexão com o DataBase.
    set_tablepvd() #Executando comando para limpar os produtos do caixa. 
    principal.ent_subtotalcaixa.setText("") #Setando valor do sub total. 

#Função encarregada de gerar o numero alfanumerico do pedido.
def numpedido(): 
    global pedido #Tornando a variavel pedido global.
    caracter= string.ascii_letters + string.digits #Gerando as LETRAS e NUMEROS do alfanumerico.
    pedido= '' #Variavel que recebera o numero alfanumerico.
    for i in range(5): #Informando quantos campos vai ter o numero alfanumerico.
        pedido += choice(caracter) #Incrementando os caracteres dentro da variavel PEDIDO.
    

#Função encarregada de amazenar os dados de compras finalizadas no DataBase
def hitory_vendas():
    numpedido() #Excutando função encarregada de gerar o número do PEDIDO.
    fpagamento= principal.comboBox.currentText() #Importando a forma de pagamento selecionada pelo USER.
    cursor=con.cursor() #Conexão com o DataBase.
    entdb=("""INSERT INTO tb_vendas
	(id, produto, vl_unidade, quantidade, vl_total, forma_pagamento, data, hora, pedido)
    SELECT id, produto, vl_unidade, quantidade, vl_total, '{}', now(), now(), '{}'
    FROM tb_vendarotativa ;""".format(fpagamento, pedido)) #Codigo para inserir dados da tabela do Caixa no Historico de vendas. 
    cursor.execute(entdb) #Executando comando no DataBase.
    con.commit() #Commitando execução no DataBase

#Função encarregada de fazer a atualização do SUBTOTAL quando algum produto for removido da compra.
def att_subtotal():

    subtotal=principal.ent_subtotalcaixa.text() #Importando valores do campo SUBTOTAL da tela do caixa.

    #Comandos a serem executados dentro do DataBase.
    cursor=con.cursor() #Criando conexão com o DataBase.
    selectdb=("SELECT vl_total FROM tb_vendarotativa WHERE id_pk='{}'".format(posi)) #Comando a ser executando dentro do DataBase.
    cursor.execute(selectdb) #Executando comando acima dentro do DataBase.
    valor=cursor.fetchone() #Selecionando valor do produto.
    cursor.close() #Fechando a conexão com o DataBase.

    #Calulo para chegar ao novo valor do SUBTOTAL:
    subtotal= float(subtotal) #Transformando variavel STR em FLOAT.
    valor= float(valor[0]) #Transformando variavel STR em FLOAT.
    calq_vl = (subtotal - valor) #Calculo para chegar ao novo valor do SUBTOTAL.

    principal.ent_subtotalcaixa.setText(str(calq_vl)) #Setando novo valor atualizado no campo SUBTOTAL.
    

#Função encarregada de fazer a remoção de produtos da compra.
def del_procompra():
    global posi #Tornando variavel visivel para outras funções.
    posi=position.ent_position.text() #Imporando valor inseirido pelo user no campo POSIÇÃO.
    
    att_subtotal() #Executando função para atualizar valor do SUBTOTAL.

    #Comandos a serem executados dentro do DataBase.
    cursor=con.cursor() #Criando conexão com o DataBase.
    editdb=("DELETE FROM tb_vendarotativa WHERE id_pk='{}'".format(posi)) #Comando a ser executado dentro do DataBase para remover um determinado produto.
    cursor.execute(editdb) #Executando comando acima dentro do DataBase.
    con.commit() #Commitando execução no DataBase.
    cursor.close() #Fechando conexão com o DataBase.

    position.hide() #Fechando tela de POSIÇÃO.

    set_tablepvd() #Executando função encarregada de mostrar a tabela da compra atualizada.


