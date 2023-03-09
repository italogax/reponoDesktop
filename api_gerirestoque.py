"""API encarregada de fazer a gestão do banco de dados, atualizado a quantidade de produtos em estoque."""

from tkinter import messagebox

#Conexão com o DataBase.
from api_conectDb import *

#Conexção com a tela do System.
from api_iniTelas import *

from api_caixaReg import hitory_vendas, limpa_tabrotativa

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
    qt_linhas() #Executanod função que faz a contagem da quantidade de linhas da Table no DataBase.
    qtlen= float(qtlinha) #Convertendo qt linhas para o formato float.
    while qtlen >= 0:
        qtlen= qtlen -1
        hitory_vendas() #Chamando função encarregada de inserir os dados da ultima compra dentro do DataBase.
        pro_vendidos() #Executando função para saber o produto a ser atualizado. 
        cursor=con.cursor() #Conexão com o DataBase.
        comandodb=("SELECT estoque FROM tb_produtos WHERE id='{}'".format(idvend)) #Comando a ser executado dentro do DataBase selecionando o valor do campo estoque.
        cursor.execute(comandodb) #Executando comando dentro do DataBase.
        campos= cursor.fetchone() #Selecionando conteudo do campo apresentado.
        cursor.close() #Fechando conexão com o DataBase.

        #Adconando o campo selecionado no DataBase em uma Variavel no System.
        for est in campos:
            int(est) #Alterando o tipo da VARIAVEL para INTEIRO.
            subestoque= est - qtvend #Calculo para chegar ao numero real daquele produto no estoque.

            #Caso o SUBESTOQUE seja menor que 0. EXECUTE:    
            if subestoque < 0:
                messagebox.showerror(
                    title= "Produto Indisponivel", 
                    message= """Quantidade de produto em estoque indisponivel.
                                Verficque a quantidade disponivel em estoque.""") #MessageBox informando que a quantidade de produtos informanda não esta disponivel no estoque.
                        

            else:
                cursor= con.cursor()
                esqatt=("UPDATE tb_produtos SET estoque= '{}' WHERE id= '{}'".format(subestoque, idvend)) #Comando para atualizar a quantidade do produto em estoque.
                cursor.execute(esqatt) #Executando comando dentro do DataBase.
                con.commit() #Commitando comando dentro do DataBase.
                cursor.close()
    else:
        messagebox.showinfo(title="Finalizado", message="Compra finalizada com sucesso!")
        limpa_tabrotativa() #Limpando a tabelaRotativa do caixa.
    
    
        
        
            

        

    


    

