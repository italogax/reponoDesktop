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


