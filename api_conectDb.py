"""API encarregada de fazer a conexão com o DataBase."""

import mysql.connector
from mysql import *

con=mysql.connector.connect(
    host='localhost', #Host do banco de dados.
    user='root', #User do banco de dados.
    password='291415', #Senha utilizada para acesso ao banco de dados.
    database='repono' #Nome do database.
)
    