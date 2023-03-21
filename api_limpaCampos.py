"""API encarregada de limpar os campos da dela de cadastro de produtos."""

#Importando API encarregada de mostrar as telas.
from api_iniTelas import *
from PyQt5 import uic, QtWidgets

#Função encarregada de limpar os campos na tela de cadastro de produtos.
def limp_cadProdutos():
    principal.ent_id_pro.setText("") #Setando no campo espaço em branco.
    principal.ent_produto_pro.setText("") #Setando no campo espaço em branco.
    principal.ent_quantidade_pro.setText("") #Setando no campo espaço em branco. 
    principal.ent_vlcompra_pro.setText("") #Setando no campo espaço em branco.
    principal.ent_vlvenda_pro.setText("") #Setando no campo espaço em branco.
    principal.ent_categoria_pro.setText("") #Setando no campo espaço em branco.
    principal.ent_fornecedor_pro.setText("") #Setando no campo espaço em branco.

#Função encarregada de fazeer a limpeza dos campos da tela de LOGIN.   
def limp_login():
    login.ent_user.setText("") #Esvaziando campos ent.
    login.ent_senha.setText("") #Esvaziando campos ent.  

#Função encarregada de fazer a limpeza dos campos da tela do CAIXA.
def limp_caixa():
    principal.ent_idcaixa.setText("") #Esvaziando o campo ID.
    principal.ent_produtocaixa.setText("") #Esvaziando o campo PRODUTO.
    principal.ent_valorcaixa.setText("") #Esvaziando o campo VALOR UNI.
    principal.ent_qtcaixa.setText("") #Esvaziando o campo QUANTIDADE.


#Função encarregada de limpar os campos da tela de cadastro de clientes.
def limp_cadclientes():
    principal.ent_id_cli.setText("") #Limpando o campo ID na tela CLIENTES.
    principal.ent_nome_cli.setText("") #Limpando o campo NOME na tela CLIENTES.
    principal.ent_email_cli.setText("") #Limpando o campo EMAIL na tela CLIENTES.
    principal.ent_contato_cli.setText("") #Limpando o campo TELEFONE na tela CLIENTES.
    principal.ent_nascimento_cli.setText("") #Limpando o campo NASCIMENTO na tela CLIENTES.
    principal.ent_cpf_cli.setText("") #Limpando o campo CPF na tela CLIENTES.


#Função encarregada de limpar os campos da tela de cadastro de FORNECEDORES.
def limp_cadfornecedores():
    principal.ent_id_for.setText("") #Limpando o campo ID na tela FORNECEDORES.
    principal.ent_nome_for.setText("") #Limpando o campo NOME na tela FORNECEDORES.
    principal.ent_email_for.setText("") #Limpando o campo EMAIL na tela FORNECEDORES.
    principal.ent_telefone_for.setText("") #Limpando o campo TELEFONE na tela FORNECEDORES.
    principal.ent_cnpj_for.setText("") #Limpando o campo CNPJ na tela FORNECEDORES.
    

#Função encarregada de limpar os campos da tela de cadastro de FUNCIONARIOS.
def limp_cadfuncionarios():
    principal.ent_id_fun.setText("") #Limpando o campo ID de cadastro de FUNCIONARIOS.
    principal.ent_nome_fun.setText("") #Limpando o campo NOME de cadastro de FUNCIONARIOS.
    principal.ent_nascimento_fun.setText("") #Limpando o campo NASCIMENTO de cadastro de FUNCIONARIOS.
    principal.ent_email_fun.setText("") #Limpando o campo EMAIL de cadastro de FUNCIONARIOS.
    principal.ent_contato_fun.setText("") #Limpando o campo CONTATO de cadastro de FUNCIONARIOS.
    principal.ent_cpf_fun.setText("") #Limpando o campo CPF de cadastro de FUNCIONARIOS.
    principal.ent_nascimento_fun.setText("") #Limpando o campo NASCIMENTO de cadastro de FUNCIONARIOS.
    principal.ent_cargo_fun.setText("") #Limpando o campo CARGO na tela FUNCIONARIOS.
    principal.ent_endereco_fun.setText("") #Lipando o capo ENDEREÇO na tela FORNECEDORES.
    