"""Esta API é encarregada de fazer todas as modificações possiveis 
no DataBase referente a produtos.
"""

from PyQt5 import uic, QtWidgets
import PySimpleGUI as py
#Importando conexão com o banco de dados.
from api_conectDb import *
#Importando telas do System.
from api_iniTelas import *
#Importando função encarregada de limpar os campos da tela de cadastro.
from api_limpaCampos import limp_cadProdutos

#Função que faz o cadastro de produtos novos no DataBase.
def cadas_produtos():
    nome=principal.ent_produto_pro.text() #Importando valores do campo PRODUTO inserido pelo user.
    quantidade=principal.ent_quantidade_pro.text() #Importando valores do campo QUANTIDADE inserido pelo user.
    vlcompra=principal.ent_vlcompra_pro.text() #Importando valores do campo VALOR COMPRA inserido pelo user.
    vlvenda=principal.ent_vlvenda_pro.text() #Importando valores do campo VALOR VENDA inserido pelo user.
    categoria=principal.ent_categoria_pro.text() #Importando valores do campo DATA ENTRADA inserido pelo user.

    cursor=con.cursor() #Conexão com o DataBase.
    entrada=""" INSERT INTO tb_produtos(id,nome,descricao,vl_compra,vl_venda,estoque) values (null,%s,%s,%s,%s,%s)""" #Comando Para inserir dados no DataBase.
    entrada2=(nome,categoria,vlcompra,vlvenda,quantidade) #Dados importandos do campo preenchido pelo user sendo inseridos no comando ENTRADA.
    cursor.execute(entrada,entrada2) #Executando comando ENTRADA, ENTRADA2
    con.commit() #Commitando dados no DataBase.
    cursor.close() #Fechando a conexão com o DataBase.
    limp_cadProdutos() #Chamando função limpa campos.

    

