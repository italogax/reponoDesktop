"""API encarregada de fazer a gestão do banco de dados, atualizado a quantidade de produtos em estoque."""

from tkinter import messagebox

#Conexão com o DataBase.
from api_conectDb import *

#Conexção com a tela do System.
from api_iniTelas import *

#Função encarre
def subestoque():
    cursor=con.cursor() #Conexão com o DataBase.
    id=principal.ent_idcaixa.text() #Importando conteudo do campo ID gerado pelo System.
    quantidade=int(principal.ent_qtcaixa.text()) #Importando conteudo do campo QUANTIDADE gerado pelo System.

    esqatt=("SELECT estoque FROM tb_produtos WHERE id='{}'".format(id)) #Comando para selecionar o campo estoque dentro do DataBase.
    cursor.execute(esqatt) #Executando comando dentro do DataBase.
    estoqueatual= cursor.fetchall() #Selecionando todos os campos da Table.

    #Selecionando o campo mostrado na table.
    for linha in estoqueatual:
        est= int((linha[0])) #Atribuindo o valor mostrado na Table.
    
    global calc
    calc= est - quantidade #Calculo para chegar ao numero real daquele produto no estoque.
    
    if(calc < 0):
        messagebox.showerror(
            title= "Produto Indisponivel", 
            message= """Quantidade de produto em estoque indisponivel.
                        Verficque a quantidade disponivel em estoque.""") #MessageBox informando que a quantidade de produtos informanda não esta disponivel no estoque

    else:
        esqatt=("UPDATE tb_produtos SET estoque= '{}' WHERE id= '{}'".format(calc, id)) #Comando para atualizar a quantidade do produto em estoque.
        cursor.execute(esqatt) #Executando comando dentro do DataBase.
        con.commit() #Commmitando comando dentro do DataBase.
    