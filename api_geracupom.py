"""API encarregada de gerar o PDF do CUPOM FISCAL do System."""

from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4 
import os

#Criando a conexão com o DataBase.
from api_conectDb import *

#Função encarregada de selecionar o primeiro ITEM da Table.
def select_item():
    global item #Tornando a variavel IDITEM global.

    cursor=con.cursor() #Criando a conexão com o DataBase.
    comandodb=("SELECT * FROM tb_vendarotativa") #Comando a ser executado dentro do DataBase.
    cursor.execute(comandodb) #Executando comando dentro do DataBase.
    item=cursor.fetchall() #Selecionando campos mostrados no DataBase.
    cursor.close() #Fechando conexão com o DataBase.

#Função encarregada de executar o PDF no acrobat.
def exe_pdf():
    caminho= ("D:\meu_pdf.pdf") #Caminho do arquivo PDF.
    cmd = "start {}".format(caminho) #Comando a ser executado para inicicar o PDF.
    exitCMD= "taskkill /f /im cmd.exe" #Comando a ser executado para FECHAR o CMD.

    os.system(cmd) #Executando comando no CMD.
    os.system(exitCMD) #Executando comando no CMD.

#Função encarregada de gerar o CUPOM fiscal.
def geracp():
    select_item() #Executando função que seleciona o ITEM no DataBase.

    #Vetor contendo os campos do CABEÇALHO de ITENS.
    campos = ['ITEM','COD  ','DESC','  QT','VL_UN','VL_TOTAL']

    pdf= canvas.Canvas("cp_vendas\Cupom_Fiscal.pdf") #Criando o arquivo.

    #PreTexto de todo cupom:
    pdf.rect(90, 100, 420, 720) #Criando controno do CUPOM
    pdf.drawString(260, 800, "Repono") #Titulo.
    pdf.drawString(100, 780, "CNPJ: 00.000.000/0001-00") #CNPJ.
    pdf.drawString(100, 760, "IE:000000000000") #IE.
    pdf.drawString(100, 740, "IM:000000000000") #IM.
    pdf.line(100, 720, 500, 720) #Linha Divisoria.
    pdf.drawString(250, 700, "CUPOM FISCAL") #Titulo.

    #Cabeçalho de itens do CUPOM FISCAL:
    espaco = 115 #Espaçamento entre itens.
    #Selecionando todos os nomes do vetor CAMPOS
    for cm in campos: 
        pdf.drawString(espaco, 680, cm) #Inserindo os nomes selecionados dentro de CAMPOS.
        espaco += 60 #adcionando mais 30 de espaço no espaçamento entre os ITENS.

    #Setando dados do DataBase
    y= 0 #Adcionando uma variavel para ser utilizanda no posicionamento dos dados abaixo.

    #Lendo dados da tabela no DataBase.
    for i in range(0,len(item)):

        y = y + 30 #Adcionando mais 30 na medida da posição Y.
        x= 130 #Adcionando uma valor a medida da posição X.

        pdf.drawString(x, 680 -y, str(item[i][5])) #Setando dados da Table no PDF.
        x+=50 #Adcionando mais espaço na medida X.
        pdf.drawString(x, 680 -y, str(item[i][0])) #Setando dados da Table no PDF.
        x+=30 #Adcionando mais espaço na medida X.
        pdf.drawString(x, 680 -y, str(item[i][1])) #Setando dados da Table no PDF.
        x+=100 #Adcionando mais espaço na medida X.
        pdf.drawString(x, 680 -y, str(item[i][2])) #Setando dados da Table no PDF.
        x+=50 #Adcionando mais espaço na medida X.
        pdf.drawString(x, 680 -y, str(item[i][4])) #Setando dados da Table no PDF.
        x+=70 #Adcionando mais espaço na medida X.
        pdf.drawString(x, 680 -y, str(item[i][3])) #Setando dados da Table no PDF.
        x+=50 #Adcionando mais espaço na medida X.
 
    pdf.save() #Salvando PDF criado.

    exe_pdf() #Executando comando que abre arquivo PDF.
geracp()

