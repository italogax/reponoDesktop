"""Esta API é ecarregada para efetuar 
a modificação de produtos já inseridos no Database
porem precisam de alguma atualização."""

from PyQt5 import uic, QtWidgets
import PySimpleGUI as py
#Importando conexão com o banco de dados.
from api_conectDb import *
#Importando telas.
from api_iniTelas import *
#Importando função LIMPACAMPOS.
from api_limpaCampos import *

#Função encarregada para alterar os dados dos produtos já existentes no DataBase.
def alter_produtos():

    id=principal.ent_id_pro.text() #Importando valores do campo ID inseridos pelo user.
    nome=principal.ent_produto_pro.text() #Importando valores do campo PRODUTO inserido pelo user.
    quantidade=principal.ent_quantidade_pro.text() #Importando valores do campo QUANTIDADE inserido pelo user.
    vlcompra=principal.ent_vlcompra_pro.text() #Importando valores do campo VALOR COMPRA inserido pelo user.
    vlvenda=principal.ent_vlvenda_pro.text() #Importando valores do campo VALOR VENDA inserido pelo user.
    categoria=principal.ent_categoria_pro.text() #Importando valores do campo DATA ENTRADA inserido pelo user.
    fornecedor=principal.ent_fornecedor_pro.text() #Importando valores do campo FORNECEDOR inserido pelo user.
    
    #Função para fazer a verificação dos campos e detectar ce algum esta fazio
    if id == '' or nome == '' or quantidade == '' or vlcompra == '' or vlvenda == '' or categoria == '' or fornecedor == '':
        messagebox.showerror(title="Campo Vazio", message="Alteração interronpida, por favor preencha tds os campos!") #MessageBox informando que algum campo esta vazio.
    
    else:
        #Comandos dentro do SQL
        cursor=con.cursor() #Conectando ao DataBase.
        #Comando executado dentro do DataBase para gerar a atualização nos dados.
        editabanco=("UPDATE tb_produtos SET nome='{}',descricao='{}',fornecedor='{}',vl_compra='{}',vl_venda='{}',estoque='{}' WHERE id ='{}'".format(nome,categoria,fornecedor,vlcompra,vlvenda,quantidade,id))
        cursor.execute(editabanco) #Executando comando.
        con.commit() #Efetuando o commit do comando EDITABANCO.
        cursor.close() #Fechando a conexão com o DataBase.
        limp_cadProdutos() #Executando a função limpa campos, para deixar todos os campos vazios.