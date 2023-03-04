import mysql.connector
from mysql.connector import errorcode

try:
    db_connection = mysql.connector.connect(
    host='localhost',
    user='root', 
    password='291415', 
    database='repono')
    cursor =db_connection.cursor()
    checkbanco=(
        "SELECT id, cpf FROM tb_funcionario WHERE id = '{}' AND cpf = '{}".format());
    cursor.execute(checkbanco)
    
    print("Conexão realizada com sucesso!")

except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)
else:
	db_connection.close()


from mysql.connector import (connection)
db_connection = connection.MySQLConnection(
  host='127.0.0.1', 
  user='root',
  password='291415',
  database='repono')
db_connection.close()