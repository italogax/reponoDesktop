"""API encarregada de fazer a remoção de produtos dentro do DATA BASE."""

from PyQt5 import uic, QtWidgets
import PySimpleGUI as py
#Importando conexão com o banco de dados.
from api_conectDb import *
#Importando telas.
from api_iniTelas import *
#Importando função LIMPACAMPOS.
from api_limpaCampos import *

#Função encarregada de remover produtos do banco de dados.
def remo_produtos():

    id=principal.ent_id_pro.text() #Importando valores do campo ID inseridos pelo user.
    cursor=con.cursor() #Gerando a conexão com DataBase.

    editabanco=("DELETE FROM tb_produtos WHERE id='{}'".format(id)) #Comando a ser executado dentro do DataBase para deletar uma linha.
    cursor.execute(editabanco) #Executando comando dentro do DataBase.
    cursor.close() #Fechando a conexão do DataBase 

    limp_cadProdutos() #Chamando função para limpar todos os campos da tela de CADASTRPO DE PRDODUTOS.

    
