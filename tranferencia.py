
import sys

#PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

#from  import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk




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
    entdb=(""""""INSERT INTO tb_vendas
	(id, produto, vl_unidade, quantidade, vl_total, forma_pagamento, data, hora, pedido)
    SELECT id, produto, vl_unidade, quantidade, vl_total, '{}', now(), now(), '{}'
    FROM tb_vendarotativa ;"""""".format(fpagamento, pedido)) #Codigo para inserir dados da tabela do Caixa no Historico de vendas. 
    cursor.execute(entdb) #Executando comando no DataBase.
    con.commit() #Commitando execução no DataBase
    
#hitory_vendas()
fpagamento= principal.comboBox.currentText()
print (fpagamento )
"""
"""
#Criando JANELA para escolher qual produto deve ser removido.
jan= Tk() #Criando a JANELA tkinter.
jan.title("Cancelamento de produto") #Inserindo um titulo nessa JANELA.
jan.geometry("250x150") #Informando as dimenções dessa JANELA.
jan.configure(background= "white") #Indicando uma cor para o fundo dessa JANELA.
jan.resizable(width=False, height=False) #

#========= WIDGETS ============
Frame = Frame(jan, width=250, height=150, bg="GRAY", relief="raise") #Criando FRAME direito.
Frame.pack(side=RIGHT) #Selecionando o lado do FRAME.

Labeltext = Label(Frame, text="Digite a posição do produto:", font=("Century Gothic", 10), bg="GRAY", fg="Black") #Criando texto idicativo.
Labeltext.place(x=30, y=30) #Posicionando o campo LABEL.

UserEntry = ttk.Entry(Frame, width=30) #Criando o campo de entrada do USER.
UserEntry.place(x=35, y=55) #Posicionando o campo USER.

bt_remover = Button(jan, text="Remover", bd="white", command= jan.destroy)
bt_remover.place(x=35, y=70)

jan.mainloop()
"""
"""
def att_subtotal():

    subtotal= 1000 #Importando valores do campo SUBTOTAL da tela do caixa.

    #Comandos a serem executados dentro do DataBase.
    cursor=con.cursor() #Criando conexão com o DataBase.
    selectdb=("SELECT vl_total FROM tb_vendarotativa WHERE id_pk='{}'".format(1)) #Comando a ser executando dentro do DataBase.
    cursor.execute(selectdb) #Executando comando acima dentro do DataBase.
    valor=cursor.fetchone() #Selecionando valor do produto.
    cursor.close() #Fechando a conexão com o DataBase.

    #Calulo para chegar ao novo valor do SUBTOTAL:
    subtotal= float(subtotal) #Transformando variavel STR em FLOAT.
    valor= float(valor[0]) #Transformando variavel STR em FLOAT.
    calqsub = subtotal - valor #Calculo para chegar ao novo valor do SUBTOTAL.

    #subtotal=principal.ent_subtotalcaixa.setText(str(calqsub)) #Setando novo valor atualizado no campo SUBTOTAL.
    print(calqsub)
    print(valor)

att_subtotal()
"""
"""
def criarPDF():
    cnv= canvas.Canvas("test.pdf", pagesize=A4) #Gerando o arquivo PDF.

app=Tk()
app.title("TESTE DE PDF")
app.geometry("600x300")

btn_criaPDF=Button(app, text="CRIA PDF", command=criarPDF)
btn_criaPDF.pack(side="left", padx=10)

app.mainloop()
"""
"""
def comando1():
        
    id=principal.ent_id_pro.text() #Importando valores inseridos pelo user no campo ID.

    cursor=con.cursor()
    editdb=("SELECT * FROM tb_produtos WHERE id='{}'".format(id))
    cursor.execute(editdb)
    campos=cursor.fetchall() #Selecionando todos os campos mostrados no DataBase.

    principal.ent_produto_pro.setText(str(campos[0][1])) #Setando a primeira coluna.
    principal.ent_categoria_pro.setText(str(campos[0][2])) #Setando a segunda coluna.
    principal.ent_fornecedor_pro.setText(str(campos[0][3])) #Setando a terceira coluna.
    principal.ent_quantidade_pro.setText(str(campos[0][6])) #Setando a quinta coluna.
    principal.ent_vlcompra_pro.setText(str(campos[0][4])) #Setando a terceira coluna.
    principal.ent_vlvenda_pro.setText(str(campos[0][5])) #Setando a quarta coluna.

def consul_produtos_ids():

    id=principal.ent_id_pro.text() #Importando valores inseridos pelo user no campo ID.

    cursor=con.cursor() #Conexão no DataBase.
    editabanco=("SELECT * FROM tb_produtos WHERE id= '{}'".format(1)) #Comando que seleciona a coluna a partir do ID.
    cursor.execute(editabanco) #Executando o EDITABANCO dentro do DataBase.
    veriProduto = cursor.fetchone() #Selecionando toda a linha com as colunas no DataBase.
    cursor.close() #Fechando a conexão com o DataBase
    try:
        if(id in veriProduto):
            print(id)

            
    except:        
        #MessageBox informando que o ID não foi encontrado.
        messagebox.showerror(title="Id não encontrado", message="""
"""ID não encontrado!Por favor verficque na aba INVENTARIO o ID que procura!"""
 


def produtos_vd():

    #Comandos a serem executados dentro do DataBase.
    cursor=con.cursor() #Criando conexão com o DataBase.
    comandodb=("SELECT * FROM tb_vendarotativa") #Comando a ser executado dentro do DataBase.
    cursor.execute(comandodb) #Executando comando dentro do DataBase.
    itens=cursor.fetchall() #Selecionando todos campos da tabela.
    
    print(itens[0][0])

produtos_vd()

"""#Função encarregada de importar os intes vendidos na compra
def produtos_vd():
    qt_linhas() #Executando função que conta quantas linhas tem no DataBase.
    select_item() #Função encarregada de selecionar ITEM no DataBase.
    qtlen = qtlinha #Atribuindo o valor da quantidade de linhas da TABLE a uma outra Variavel.
    #Laço de repetição.
    while qtlen > 0:  
        qtlen = qtlen - 1 #Subtraindo 1 na quantidade de linhas. 
        #Comandos a serem executados dentro do DataBase.
        cursor=con.cursor() #Criando conexão com o DataBase.
        comandodb=("SELECT * FROM tb_vendarotativa WHERE id='{}'".format(qtlen)) #Comando a ser executado dentro do DataBase.
        cursor.execute(comandodb) #Executando comando dentro do DataBase.
        itens=cursor.fetchall() #Selecionando todos campos da tabela.
        for it in itens:
            print(it)"""

"""#Função encarregada de verificar quantas linhas tem na table tb_vendarotativa.
def qt_linhas():
    global qtlinha
    cursor=con.cursor() #Conexão com o DataBase.
    comandodb=("SELECT COUNT(id) FROM tb_vendarotativa") #Comando a ser executado dentro do DataBase para identificar quantas linhas há na tb_vendarotativa.
    cursor.execute(comandodb) #Executando comando dentro do DataBase.
    max= cursor.fetchone()
    cursor.close()
    for qtlinha in max:
        qtlinha= float(qtlinha)"""