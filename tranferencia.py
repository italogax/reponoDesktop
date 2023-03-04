from PyQt5 import uic, QtWidgets # Import do Pyqt5
import mysql
import mysql.connector

    atendente= tl_principal.ent_atendente.setText()

    idcaixa= tl_principal.ent_idcaixa.setText()

    produtos= tl_principal.ent_produtocaixa.setText()

    quantidade= tl_principal.ent_qtcaixa.setText()

    subtotal= tl_principal.ent_subtotalcaixa.setText()

    valocaixa= tl_principal.ent_valorcaixa.setText()


    estoque = ("select estoque from tb_produtos where produto = '{}'").format(produtos) # Função para buscar quantidade atual do estoque
    cursor = connect.cursor()
    cursor.execute(estoque)
    linhas= cursor.fetchall()

    for linha in linhas:

        est= int((linha[0]))    # função para trasnformar quatindade atual do estoque em INTEIRO

    conta = est - quantidade # conta para diminuir quantidade vendida no estoque

    if (conta <= 0): #Função de verificaçao de estoque
        resul = tl_principal.resul.setText("Estoque faltando") #Mensagem de estoque em falta

    else: #Função de verificaçao de estoque

        att= ("update tb_produtos set estoque = '{}' where nome = '{}'").format(conta,produtos) #Função para atualizar quantidade do estoque no banco de dados

        att_cur = connect.cursor()

        att_cur.execute(att)

        confi = "insert into tb_vendas(id, produto, vl_venda, funcionario, quantidade, forma_pagamento, desconto, data, hora) values (null, %s, %s, %s, %s, %s, %s, now(),now())" #Função para inserir venda no banco de dados

        dados = (prod, quant) # dados para inserir na tabela

        cursor = connect.cursor()

        cursor.execute(confi, dados)

        connect.commit()

        cursor.close()

# --Iniciar tela-- #

tl_principal.bt_finalizarcompra.clicked.connect(tela)

tl_principal.show()

app.exec()





