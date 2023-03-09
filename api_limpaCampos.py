"""API encarregada de limpar os campos da dela de cadastro de produtos."""

#Importando API encarregada de mostrar as telas.
from api_iniTelas import *
from PyQt5 import uic, QtWidgets

#Função encarregada de limpar os campos na tela de cadastro de produtos.
def limp_cadProdutos():
    id=principal.ent_id_pro.setText("") #Setando no campo espaço em branco.
    nome=principal.ent_produto_pro.setText("") #Setando no campo espaço em branco.
    quantidade=principal.ent_quantidade_pro.setText("") #Setando no campo espaço em branco. 
    vlcompra=principal.ent_vlcompra_pro.setText("") #Setando no campo espaço em branco.
    vlvenda=principal.ent_vlvenda_pro.setText("") #Setando no campo espaço em branco.
    categoria=principal.ent_categoria_pro.setText("") #Setando no campo espaço em branco.
    fornecedores=principal.ent_fornecedor_pro.setText("") #Setando no campo espaço em branco.

#Função encarregada de fazeer a limpeza dos campos da tela de LOGIN.   
def limp_login():
    usuario= login.ent_user.setText("") #Esvaziando campos ent.
    psword= login.ent_senha.setText("") #Esvaziando campos ent.  

#Função encarregada de fazer a limpeza dos campos da tela do CAIXA.
def limp_caixa():
    id=principal.ent_idcaixa.setText("") #Esvaziando o campo ID.
    produto=principal.ent_produtocaixa.setText("") #Esvaziando o campo PRODUTO.
    valoruni=principal.ent_valorcaixa.setText("") #Esvaziando o campo VALOR UNI.
    quantidade=principal.ent_qtcaixa.setText("") #Esvaziando o campo QUANTIDADE.