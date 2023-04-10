"""API encarregada de fazer a demonstração das telas do System. """

import sys
from tkinter import messagebox
from PyQt5 import uic, QtWidgets
import PySimpleGUI as py

app = QtWidgets.QApplication ([])

#Função chama tela Princiapal================================================
def chama_tl_principal():
    principal.show()
    login.hide()

#Variaveis de telas-------------------------------------------------
login = uic.loadUi('tl_log.ui') #Variavel responsavel pela tela de login.
principal = uic.loadUi('tl_principal.ui') #Variavel responsavel pela tela principal
position = uic.loadUi('tl_position.ui') #Variavel responsavel pela tela posição do produto na compra.
cupom = uic.loadUi('tl_cupomfiscal.ui') #Variavel responsavel pela tela onde o CUPOM FISCAL ira ser demonstrado.

#Função chama tela Posição do Item================================================
def chama_tl_position():
    position.show()
    
#Função chama tela PDF================================================
def chama_tl_cupom():
    cupom.show()

