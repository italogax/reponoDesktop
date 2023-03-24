"""Codigo Fonte que faz todas as conexões."""

import sys
from tkinter import messagebox
from PyQt5 import uic, QtWidgets
import PySimpleGUI as py
import keyboard
#Importando conexão com DATABASE.
from api_conectDb import * 
#Importando verificação do USER e PSWORD.
from api_checkuser import *
#Importando função cadastro de produtos.
from api_cadProdutos import *
#Importando função alteração de produtos.
from api_altProdutos import *
#Importando função para consulta produtos
from api_conProdutos import consul_produtos_id, consul_produtos
#Importando função que deleta produtos do DataBase.
from api_delProdutos import remo_produtos
#Importando função do PVD.
from api_caixaReg import check_conteudo, sub_total, limpa_tabrotativa, del_procompra 
#Importando Aplicação referente a todas as funções que fazer o trabalho de baixa no estoque.
from api_gerirestoque import *
#Imporando função que cadastra clientes.
from api_cadcliente import  *
#Imporando função que altera cadastro de clientes.
from api_altcliente import *
#Imporando função que consulta cadastro de clientes.
from api_concliente import *
#Imporando função que deleta cadastro de clientes.
from api_delcliente import *
#Importando função que cadastra Fornecedore.
from api_cadfornecedores import *
#Importando função que consulta dados dos FORNECEDORES dentro do DataBase e retorna esses dados na tela FORNECEDORES.
from api_confornecedores import *
#Importando função que faz alterações de dados já existentes dentro do DataBase.
from api_altfornecedores import *
#Importando função encarregada de DELETAR cadastro de fornecedores no DataBase.
from api_delfornecedores import *
#Importando função encarregada de DELETAR cadastro de funcionarios no DataBase.
from api_delfuncionarios import *
#Importando função encarregada de CONSULTAR cadastro de funcionarios no DataBase.
from api_confuncionarios import *
#Importando função encarregada de CADASTRAR novos funcionarios no DataBase.
from api_cadfuncionarios import *
#Importando função encarregada de ALTERAR dados de FUNCIONARIOS já existentes.
from api_altfuncionarios import *


from tranferencia import *


#Bottons do System======================================================================
#Tela de login------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
login.bt_entrar.clicked.connect(check_user) #Click botton entrar inicia a def checkuser.

#Tela clientes------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
principal.bt_cadas_pro.clicked.connect(cadas_produtos) #Botão cadastrar que chama a função cadastro de produtos.
principal.bt_atualizar_pro.clicked.connect(alter_produtos) #Botão atualizar que chama a função alterar dados do produto.
principal.bt_consulta_pro.clicked.connect(consul_produtos_id) #Botão consultar que chama a função consultar produtos pelo ID. 
principal.bt_inventario.clicked.connect(consul_produtos)  #Botão inventario que mostra todos os dados existentes na table do DataBase.
principal.bt_remover_pro.clicked.connect(remo_produtos) #Botão remover que chama a função remover produtos no DataBase.
principal.bt_limpar_pro.clicked.connect(limp_cadProdutos) #Botão limpa campos que chama a função para limpar todos os campos da tela de cadastro de produtos.

#Tela do Caixa=========================================================================================================================================================================================================================
principal.bt_cancelarcompra.clicked.connect(limpa_tabrotativa) #Botão encarregado de cancelar a compra que estava sendo efetuada.
principal.bt_cancelarproduto.clicked.connect(chama_tl_position) #Botão encarregado de cancelar produtos expecificos da compra.
principal.bt_finalizarcompra.clicked.connect(att_estoque) #Botão encarregado de finalizar a compra.
principal.bt_pesquisar.clicked.connect(check_conteudo) #Botão encarregado de pesquisar o valor unitario e o nome do produto.
principal.bt_calq.clicked.connect(sub_total) #Botão encarregado de fazer o calculo do subtotal.
#principal.bt_tabcodigos_ven.clicked.connect(consul_produtos)

#Tel Posição-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
position.bt_remover.clicked.connect(del_procompra) #Botão encarregado de fazer a remoção de um produto especifico na compra.

#Tela de Pessoas=========================================================================================================================================================================================================================
#Tela Cadastro de Clientes---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
principal.bt_cadas_cli.clicked.connect(cad_clientes) #Botão encarregado de fazer o cadastro de CLIENTES.
principal.bt_consulta_cli.clicked.connect(verifi_clientes) #Botão encarregado de fazer consulta de dados dentro do DataBase e retornar os dados na tela de CLIENTES.
principal.bt_atualizar_cli.clicked.connect(alter_clientes) #Botão encarregado de fazer alterações no cadastro de CLIENTES.
principal.bt_remover_cli.clicked.connect(remo_clientes) #Botão encarregado de fazer o DELETE de dados de CLIENTES no DataBase.
principal.bt_limpar_cli.clicked.connect(limp_cadclientes) #Botão encarregado de fazer a limpeza dos campos da tela CLIENTES.

#Tela Cadastro de Fornecedores-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
principal.bt_cadas_for.clicked.connect(cad_fornecedores) #Botão encarregado de cadastrar novos FORNECEDORES no DataBase.
principal.bt_consulta_for.clicked.connect(con_fornecedores) #Botão encarregado de consultar e retornar dados do DataBase na tela FORNECEDORES.
principal.bt_atualizar_for.clicked.connect(alter_fornecedores) #Botão encarregado de fazer alteraçõess em dados já existentes dentro do DataBase na table FORNECEDORES.
principal.bt_remover_for.clicked.connect(remo_fornecedores) #Botão encarregado de fazer o DELETE CLIENTES do DataBase.
principal.bt_limpar_for.clicked.connect(limp_cadfornecedores) #Botão encarregado de fazer a limpeza dos campos da tela FORNECEDORES.

#Tela Cadastro de Funcionarios-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
principal.bt_cadas_fun.clicked.connect(cad_funcionarios) #Botão encarregado de cadastrar novos FUNCIONARIOS no DataBase.
principal.bt_consulta_fun.clicked.connect(veri_funcionarios) #Botão encarregado de fazer a CONSULTA de dados no DataBase e rotarnando esses dados na tela FUNCIONARIOS.
principal.bt_atualizar_fun.clicked.connect(alter_funcionarios) #Botão encarregado de fazer as ALTERAÇÕES de dados de FUNCIONARIOS no DataBase.
principal.bt_remover_fun.clicked.connect(remo_funcionarios) #Botão encarregado de fazer o DELETE FUNCIONARIOS do DataBase.
principal.bt_limpar_fun.clicked.connect(limp_cadfuncionarios) #Botão encarregado de fazer a limpeza dos campos da tela FUNCIONARIOS.

limpa_tabrotativa() #Executando função encarregada de fazer a limpeza da TAB_VENDAROTATIVA.
login.show() #Exibi tela login.
app.exec() #Executar sistema.