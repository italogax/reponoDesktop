from api_conectDb import *
"""Codigo Fonte que faz todas as conexões."""

import sys
from tkinter import messagebox
from PyQt5 import uic, QtWidgets
import PySimpleGUI as py
import keyboard
#Importando conexão com DATABASE.
from api_conectDb import * 
#Importando verificação do USER e PSWORD.
from api_checkuser import *
#Importando função cadastro de produtos.
from api_cadProdutos import *
#Importando função alteração de produtos.
from api_altProdutos import *
#Importando função para consulta produtos
from api_conProdutos import *
#Importando função que deleta produtos do DataBase.
from api_delProdutos import *
#Importando função do PVD.
from api_caixaReg import *
#Importando Aplicação referente a todas as funções que fazer o trabalho de baixa no estoque.
from api_gerirestoque import *
#Importando funções que automatizam processos no teclado.
from api_atalhoskey import keypress



"""
cursor=con.cursor() #Conexão com o DataBase.
comandodb=("SELECT COUNT(id) FROM tb_vendarotativa") #Comando a ser executado dentro do DataBase para identificar quantas linhas há na tb_vendarotativa.
cursor.execute(comandodb) #Executando comando dentro do DataBase.
qtlinha= cursor.fetchone()
cursor.close()

for qt in qtlinha:
    print (int(qt))
"""
"""
cursor=con.cursor() #Conexão com o DataBase.
comandodb=("SELECT estoque FROM tb_produtos WHERE id='{}'".format(1)) #Comando a ser executado dentro do DataBase selecionando o valor do campo estoque.
cursor.execute(comandodb) #Executando comando dentro do DataBase.
campos= cursor.fetchone() #Selecionando conteudo do campo apresentado.
cursor.close()
for est in campos:
     print(int(est))
"""
"""
def test():
    global idvend #Tornando a VARIAVEL em GLOBAL. 
    global qtvend #Tornando a VARIAVEL em GLOBAL. 
    cursor=con.cursor() #Conexão com o DataBase.
    comandodb=("SELECT id, quantidade FROM tb_vendarotativa") #Comando a ser executado dentro do DataBaese.
    cursor.execute(comandodb) #Executando comando dentro do DataBase. 
    vendidos=cursor.fetchall()  #Selecionando todos os campos apresentados na tabela.
    cursor.close() #Fechando conexão com o DataBase.
    idvend= (vendidos[0][0]) #Atribuindo valor a Variavel IDVEND, valor:(primeiro ID da TABLE.)
    qtvend= (vendidos[0][1]) #Atribuindo valor a Variavel QTVEND, valor:(primeiro QUANTIDADE da TABLE.)

def test3():
    test()
    print (idvend)
    print (qtvend)
test3()
"""
"""
cursor=con.cursor() #Conexão com o DataBase.
comandodb=("SELECT COUNT(id) FROM tb_vendarotativa") #Comando a ser executado dentro do DataBase para identificar quantas linhas há na tb_vendarotativa.
cursor.execute(comandodb) #Executando comando dentro do DataBase.
max= cursor.fetchone()
cursor.close()
for qtlinha in max:
    int(qtlinha)

i= 1
while i < qtlinha:
    i= i + 1
    hitory_vendas() #Chamando função encarregada de inserir os dados da ultima compra dentro do DataBase.
    pro_vendidos() #Executando função para saber o produto a ser atualizado. 
    cursor=con.cursor() #Conexão com o DataBase.
    comandodb=("SELECT estoque FROM tb_produtos WHERE id='{}'".format(idvend)) #Comando a ser executado dentro do DataBase selecionando o valor do campo estoque.
    cursor.execute(comandodb) #Executando comando dentro do DataBase.
    campos= cursor.fetchone() #Selecionando conteudo do campo apresentado.
    cursor.close()
    for est in campos:
        int(est)
        subestoque= est - qtvend #Calculo para chegar ao numero real daquele produto no estoque.
                
        if(subestoque < 0):
                print ("erro")
                        

        else:
            esqatt=("UPDATE tb_produtos SET estoque= '{}' WHERE id= '{}'".format(subestoque, idvend)) #Comando para atualizar a quantidade do produto em estoque.
            cursor.execute(esqatt) #Executando comando dentro do DataBase.
            con.commit() #Commitando comando dentro do DataBase.
            cursor.close()
"""
"""
def qt_linhas():
    global qtlinha
    cursor=con.cursor() #Conexão com o DataBase.
    comandodb=("SELECT COUNT(id) FROM tb_vendarotativa") #Comando a ser executado dentro do DataBase para identificar quantas linhas há na tb_vendarotativa.
    cursor.execute(comandodb) #Executando comando dentro do DataBase.
    max= cursor.fetchone()
    cursor.close()
    for qtlinha in max:
        float(qtlinha)

qt_linhas()
print (float(qtlinha))
print (type(qtlinha))
"""
"""
def qt_linhas():
    global conversor
    cursor=con.cursor() #Conexão com o DataBase.
    comandodb=("SELECT COUNT(id) FROM tb_vendarotativa") #Comando a ser executado dentro do DataBase para identificar quantas linhas há na tb_vendarotativa.
    cursor.execute(comandodb) #Executando comando dentro do DataBase.
    max= cursor.fetchone()
    cursor.close()
    for qtlinha in max:
        conversor= float(qtlinha)


def test2():
    qt_linhas()
    print (conversor)
test2()
"""
"""
"""
def numpedido(): 
    global pedido #Tornando a variavel pedido global.
    caracter= string.ascii_letters + string.digits #Gerando as LETRAS e NUMEROS do alfanumerico.
    pedido= '' #Variavel que recebera o numero alfanumerico.
    for i in range(5): #Informando quantos campos vai ter o numero alfanumerico.
        pedido += choice(caracter) #Incrementando os caracteres dentro da variavel PEDIDO.
    
def hitory_vendas():
    numpedido() #
    fpagamento= principal.comboBox.currentText()
    cursor=con.cursor() #Conexão com o DataBase.
    entdb=("""INSERT INTO tb_vendas
	(id, produto, vl_unidade, quantidade, vl_total, forma_pagamento, data, hora, pedido)
    SELECT id, produto, vl_unidade, quantidade, vl_total, '{}', now(), now(), '{}'
    FROM tb_vendarotativa ;""".format(fpagamento, pedido)) #Codigo para inserir dados da tabela do Caixa no Historico de vendas. 
    cursor.execute(entdb) #Executando comando no DataBase.
    con.commit() #Commitando execução no DataBase
    
#hitory_vendas()
fpagamento= principal.comboBox.currentText()
print (fpagamento )