# Form implementation generated from reading ui file 'c:\Users\Italo\OneDrive\reponoDesktop\widgets\tl_cadascliente.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fr_clientes = QtWidgets.QWidget(parent=self.centralwidget)
        self.fr_clientes.setGeometry(QtCore.QRect(0, 70, 801, 381))
        self.fr_clientes.setStyleSheet("background-color: rgb(241, 241, 241);\n"
"border-radius:10px;")
        self.fr_clientes.setObjectName("fr_clientes")
        self.label_15 = QtWidgets.QLabel(parent=self.fr_clientes)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.label_15.setObjectName("label_15")
        self.label_idC = QtWidgets.QLabel(parent=self.fr_clientes)
        self.label_idC.setGeometry(QtCore.QRect(10, 100, 31, 16))
        self.label_idC.setObjectName("label_idC")
        self.ent_id_clientes = QtWidgets.QLineEdit(parent=self.fr_clientes)
        self.ent_id_clientes.setGeometry(QtCore.QRect(40, 90, 71, 41))
        self.ent_id_clientes.setStyleSheet("QLineEdit {\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.ent_id_clientes.setObjectName("ent_id_clientes")
        self.label_nomeC = QtWidgets.QLabel(parent=self.fr_clientes)
        self.label_nomeC.setGeometry(QtCore.QRect(140, 100, 61, 16))
        self.label_nomeC.setObjectName("label_nomeC")
        self.ent_nome_clientes = QtWidgets.QLineEdit(parent=self.fr_clientes)
        self.ent_nome_clientes.setGeometry(QtCore.QRect(200, 90, 431, 41))
        self.ent_nome_clientes.setStyleSheet("QLineEdit {\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.ent_nome_clientes.setObjectName("ent_nome_clientes")
        self.label_cpfC = QtWidgets.QLabel(parent=self.fr_clientes)
        self.label_cpfC.setGeometry(QtCore.QRect(10, 170, 41, 21))
        self.label_cpfC.setObjectName("label_cpfC")
        self.ent_cpf_clientes = QtWidgets.QLineEdit(parent=self.fr_clientes)
        self.ent_cpf_clientes.setGeometry(QtCore.QRect(50, 160, 131, 41))
        self.ent_cpf_clientes.setStyleSheet("QLineEdit {\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.ent_cpf_clientes.setObjectName("ent_cpf_clientes")
        self.label_dt_nascimentoC = QtWidgets.QLabel(parent=self.fr_clientes)
        self.label_dt_nascimentoC.setGeometry(QtCore.QRect(200, 170, 181, 16))
        self.label_dt_nascimentoC.setObjectName("label_dt_nascimentoC")
        self.ent_dt_nascimento = QtWidgets.QLineEdit(parent=self.fr_clientes)
        self.ent_dt_nascimento.setGeometry(QtCore.QRect(400, 160, 131, 41))
        self.ent_dt_nascimento.setStyleSheet("QLineEdit {\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.ent_dt_nascimento.setObjectName("ent_dt_nascimento")
        self.label_contatoC = QtWidgets.QLabel(parent=self.fr_clientes)
        self.label_contatoC.setGeometry(QtCore.QRect(10, 230, 81, 16))
        self.label_contatoC.setObjectName("label_contatoC")
        self.ent_contato_clientes = QtWidgets.QLineEdit(parent=self.fr_clientes)
        self.ent_contato_clientes.setGeometry(QtCore.QRect(90, 220, 131, 41))
        self.ent_contato_clientes.setStyleSheet("QLineEdit {\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.ent_contato_clientes.setObjectName("ent_contato_clientes")
        self.label_emailC = QtWidgets.QLabel(parent=self.fr_clientes)
        self.label_emailC.setGeometry(QtCore.QRect(240, 230, 51, 16))
        self.label_emailC.setObjectName("label_emailC")
        self.ent_email_clientes = QtWidgets.QLineEdit(parent=self.fr_clientes)
        self.ent_email_clientes.setGeometry(QtCore.QRect(300, 220, 361, 41))
        self.ent_email_clientes.setStyleSheet("QLineEdit {\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.ent_email_clientes.setObjectName("ent_email_clientes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_15.setText(_translate("MainWindow", "Cadastro de Clientes"))
        self.label_idC.setText(_translate("MainWindow", "ID"))
        self.label_nomeC.setText(_translate("MainWindow", "Nome"))
        self.label_cpfC.setText(_translate("MainWindow", "CPF"))
        self.ent_cpf_clientes.setInputMask(_translate("MainWindow", "999.999.999-99"))
        self.label_dt_nascimentoC.setText(_translate("MainWindow", "Data de Nascimento"))
        self.ent_dt_nascimento.setInputMask(_translate("MainWindow", "99/99/9999"))
        self.label_contatoC.setText(_translate("MainWindow", "Contato"))
        self.ent_contato_clientes.setInputMask(_translate("MainWindow", "(99)99999-9999"))
        self.label_emailC.setText(_translate("MainWindow", "Email"))
