"""Esta API é encarregada de fazer a verificação de USER e SENHA dentro do DataBase e desbloquear o APP."""

from tkinter import messagebox
from PyQt5 import uic, QtWidgets
import PySimpleGUI as py
#Importando conexão com o DataBase.
from api_conectDb import *
#Importando telas do System.
from api_iniTelas import *
#Importando função que limpa os campos da tela login.
from api_limpaCampos import limp_login

#Função para verificar USER e PSWORD no DataBase.
def check_user():
    global user
    usuario = login.ent_user.text() #Puxando conteudo inserido pelo user do campo senha.
    psword = login.ent_senha.text() #Puxando conteudo inserirdo pelo user do campo senha.
    cursor =con.cursor() #Conexão com o banco de dados.
    cursor.execute("""
    SELECT * FROM tb_funcionario
    WHERE (cargo = '{}' and cpf = '{}')
    """.format(usuario, psword)) # Execução do comando dentro do DataBase selecionando o ID e o CPF retorn no usuario e psword.

#Variavel responsavel pela comparação dos dados==================================================================
    VeriyLogin = cursor.fetchone() #Comando que busca apenas um dado dentro do DataBase.
    try:
        if (usuario in VeriyLogin and psword in VeriyLogin): #Pesquisando se o USUARIO, PSWORD estão dentro do DataBase.
            messagebox.showinfo(title= "Aviso de Login", message= "Login efetuado com sucesso, seja bem vindo!") #MessageBox informando que acessou com sucesso o sistema.
            chama_tl_principal() #Show tl Principal.

    except:
        messagebox.showerror(title="Aviso de Login", message="Acesso negado, Verifique se esta cadastrado no sistema!") #MessageBox informando que o user e senha esta incorreto.
        limp_login()#Função que limpa os campos da tela login.



    