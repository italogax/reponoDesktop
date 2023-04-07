"""API encarregada de gerar o PDF do CUPOM FISCAL do System."""

from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4 

campos = ['ITEM','CODIGO ','DESCRIÇÃO','QT','VL_UN','VL_TOTAL']



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
espaco = 100 #Espaçamento entre itens.
#Selecionando todos os nomes do vetor CAMPOS
for cm in campos: 
    pdf.drawString(espaco, 680, cm) #Inserindo os nomes selecionados dentro de CAMPOS.
    espaco += 60 #adcionando mais 30 de espaço no espaçamento entre os ITENS.


pdf.save() #Salvando PDF criado. 