"""Está API é encarregada de efetuar as consultas no DataBase e retornar dados dos
    produtos tanto na tela de cadastrar dados quanto na tela de inventario onde temos uma tabela"""

from PyQt5 import uic, QtWidgets
import PySimpleGUI as py
#Importando conexão com o banco de dados.
from api_conectDb import *
#Importando telas.
from api_iniTelas import *
#Importando função LIMPACAMPOS.
from api_limpaCampos import *

#Função para ser executada na tela principal PRODUTOS.
def consul_produtos_id():

    cursor=con.cursor() #Conexão no DataBase.
    id=principal.ent_id_pro.text() #Importando valores inseridos pelo user no campo ID.

    #Caso o campo ID esteja vazio.
    if id =="":
        #MessageBox informando que o ID não foi encontrado
        messagebox.showerror(title="Id não encontrado", message="""
        ID não encontrado!
        Por favor verficque na aba INVENTARIO o ID que procura!""")

        editabanco="SELECT * from tb_produtos" #Comando que seleciona todos os dados da DataBase.
        cursor.execute(editabanco) #Comando executando o EDITABANCO
        campos=cursor.fetchall() #Selecionando toda a linha com as colunas no DataBase.
        principal.tab_inventario.setRowCount(len(campos)) #Definindo a contagem de linhas da table.
        principal.tab_inventario.setColumnCount(6) #Definindo a contagem de colunas da table.
        for l in range(len(campos)): #Inserindo todas as linhas da DataBase na table.
            for c in range(0,6): #Inserindo todas as colunas do DataBase na table.
                principal.tab_inventario.setItem(l,c,QtWidgets.QTableWidgetItem(str(campos[l][c]))) #Setando os ITENS dentro da table.
        cursor.close() #Fechando a conexão com o DataBase.

    #Caso tenha digita algum ID no campo ID.
    else:
        editabanco=("SELECT * FROM tb_produtos WHERE id= '{}'".format(id)) #Comando que seleciona a coluna a partir do ID.
        cursor.execute(editabanco) #Executando o EDITABANCO dentro do DataBase.
        campos = cursor.fetchall() #Selecionando toda a linha com as colunas no DataBase.

        nome=principal.ent_produto_pro.setText(str(campos[0][1])) #Setando a primeira coluna.
        quantidade=principal.ent_quantidade_pro.setText(str(campos[0][5])) #Setando a quinta coluna.
        vlcompra=principal.ent_vlcompra_pro.setText(str(campos[0][3])) #Setando a terceira coluna.
        vlvenda=principal.ent_vlvenda_pro.setText(str(campos[0][4])) #Setando a quarta coluna.
        categoria=principal.ent_categoria_pro.setText(str(campos[0][2])) #Setando a segunda coluna.

#Função a ser executada apos clicar no botton INVENTARIO.
def consul_produtos():

    cursor=con.cursor() #Conexão com o DataBase.
    id=principal.ent_id_pro.text() #Importando o conteudo inserido pelo USER no campo ID.

    editabanco=("SELECT * from tb_produtos") #Comando que seleciona todas as linhas e todas as colunas no DataBase.
    cursor.execute(editabanco) #Executando comando EDITABANCO dentro do DataBase.
    campos=cursor.fetchall() #Selecionando todas as linhas, colunas do DataBase.
    principal.tab_inventario.setRowCount(len(campos)) #Definindo a contagem de linhas da table. 
    principal.tab_inventario.setColumnCount(6) #Definindo a contagem de colunas da table.
    for l in range(len(campos)): #Inserindo todas as linhas da DataBase na table.
        for c in range(0,6): #Inserindo todas as colunas do DataBase na table.
            principal.tab_inventario.setItem(l,c,QtWidgets.QTableWidgetItem(str(campos[l][c]))) #Setando os ITENS dentro da table.
    cursor.close() #Fechando a conexão com o DataBase.