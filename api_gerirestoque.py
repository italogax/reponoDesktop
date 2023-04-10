"""API encarregada de fazer a gestão do banco de dados, atualizado a quantidade de produtos em estoque."""

from tkinter import messagebox

#Conexão com o DataBase.
from api_conectDb import *

#Conexção com a tela do System.
from api_iniTelas import *

# Importando API relacionadas as vendas.
from api_caixaReg import hitory_vendas, limpa_tabrotativa

#Importando API relacionada ao gerador de CUPOM.
from api_geracupom import geracp

#Função encarregada de gerara MESSAGEBOX de erro.
def erro_finalizar():
    #Mensagem de erro.
    messagebox.showerror(title="ERRO", message="É necessario haver pelo menos 1 produto para poder finalizar uma compra.")

#Função encarregada de fazer a verificação da primeira linha da Table.   
def pro_vendidos():
    global idvend #Tornando a VARIAVEL em GLOBAL. 
    global qtvend #Tornando a VARIAVEL em GLOBAL. 
    cursor=con.cursor() #Conexão com o DataBase.
    comandodb=("SELECT id, quantidade FROM tb_vendarotativa") #Comando a ser executado dentro do DataBaese.
    cursor.execute(comandodb) #Executando comando dentro do DataBase. 
    vendidos=cursor.fetchall()  #Selecionando todos os campos apresentados na tabela.
    cursor.close() #Fechando conexão com o DataBase.
    idvend= int(vendidos[0][0]) #Atribuindo valor a Variavel IDVEND, valor:(primeiro ID da TABLE.)
    qtvend= int(vendidos[0][1]) #Atribuindo valor a Variavel QTVEND, valor:(primeiro QUANTIDADE da TABLE.)

#função encarregada de deletar as linhas da tabela VENDAROTATIVA.
def del_linha():
    cursor=con.cursor() #Conexão com o DataBase.
    comandodb=("DELETE FROM tb_vendarotativa WHERE id='{}'".format(idvend)) #Comando a ser executado dentro do DataBaese.
    cursor.execute(comandodb) #Executando comando dentro do DataBase.
    con.commit() #Commitando alteração feita dentro do DataBase.
    cursor.close() #Fechando conexão com o DataBase.

#Função encarregada de verificar quantas linhas tem na table tb_vendarotativa.
def qt_linhas():
    global qtlinha
    cursor=con.cursor() #Conexão com o DataBase.
    comandodb=("SELECT COUNT(id) FROM tb_vendarotativa") #Comando a ser executado dentro do DataBase para identificar quantas linhas há na tb_vendarotativa.
    cursor.execute(comandodb) #Executando comando dentro do DataBase.
    max= cursor.fetchone()
    cursor.close()
    for qtlinha in max:
        float(qtlinha)

#Função encarregada de fazer a att do DataBase.
def att_estoque():
    geracp() #Executando função encarregada de gerar o CUPOM FISCAL.
    qt_linhas() #Executanod função que faz a contagem da quantidade de linhas da Table no DataBase.
    qtlen= float(qtlinha) #Convertendo qt linhas para o formato float.
    while qtlen > 0:
        qtlen= qtlen -1
        hitory_vendas() #Chamando função encarregada de inserir os dados da ultima compra dentro do DataBase.
        pro_vendidos() #Executando função para saber o produto a ser atualizado. 
        del_linha() #Executando função que deleta linha da tab VENDAROTATIVA.

        cursor=con.cursor() #Conexão com o DataBase.
        comandodb=("SELECT estoque FROM tb_produtos WHERE id='{}'".format(idvend)) #Comando a ser executado dentro do DataBase selecionando o valor do campo estoque.
        cursor.execute(comandodb) #Executando comando dentro do DataBase.
        campos= cursor.fetchone() #Selecionando conteudo do campo apresentado.
        cursor.close() #Fechando conexão com o DataBase.

        #Adcionando o campo selecionado no DataBase em uma Variavel no System.
        for est in campos:
            est = int(est) #Alterando o tipo da VARIAVEL para INTEIRO.
            subestoque= est - qtvend #Calculo para chegar ao numero real daquele produto no estoque.
            cursor= con.cursor()
            esqatt=("UPDATE tb_produtos SET estoque= '{}' WHERE id= '{}'".format(subestoque, idvend)) #Comando para atualizar a quantidade do produto em estoque.
            cursor.execute(esqatt) #Executando comando dentro do DataBase.
            con.commit() #Commitando comando dentro do DataBase.
            cursor.close()
            
    messagebox.showinfo(title="Finalizado", message="Compra finalizada com sucesso!")
    limpa_tabrotativa() #Limpando a tabelaRotativa do caixa.


#Função encarregada de fazer a verificação da existencia de produtos na compra.
def verifi_comp():
    qt_linhas() #Executando função que faz a contagem da quantidade de linhas na TABLE VENDAROTATIVA no DataBase.
    
    #Caso não tenha linhas.
    if qtlinha == 0: 
        erro_finalizar() #Executando função encarregada de gerara mensagem de erro.
    
    #Caso tenha alguma linha.
    else:
        att_estoque() #Executando função encarregada de fazer a atualização no DataBase.

    
    
        
        
            

        

    


    

