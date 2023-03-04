"""API encarregada de gerar o PDF do CUPOM FISCAL do System."""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

test=("""---------------------------------------------------------------------------------------------------------------------------""")

cabecapdf= ('Loja', 'AV.', 'CNPJ:', 'IE:','{}'.format(test))


def mm2p(milimetros):
    return milimetros / 0.352777

cnv = canvas.Canvas("meu_pdf.pdf", pagesize=A4) #Gerando o arquivo PDF.

eixox=10
eixoy=280

for cabecalho in cabecapdf:
    cnv.drawString(mm2p(eixox), mm2p(eixoy), cabecalho) #Inserindo TEXT no PDF.
    cnv.drawImage("Login\PNG\icon_repono.png", 200, 280, width=200, height=100) #Inserindo imagem no PDF
    eixoy -= 5

cnv.save() #Salvando alterações no PDF.
