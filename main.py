#RHUAM PFC
#webcrawler_LINKS                         #--/--/---
#------------------------------------------------------------

import PySimpleGUI as sg
from webcrawler_LKS import *
from webcrawler_LKS2_interno import *

#--------------------------------------------01
class Tela:
    def __init__(self):
        layout = [
            [sg.T('tudo certo por aqui!')],
            [sg.Button('buscar por links externos',key=('botao_L_externo')),sg.Button('buscar links na fonte da pagina',key=('botao_L_interno'))]
        ]
        self.janela = sg.Window('janela principal').layout(layout)

#-------------------------------------------02--------------------------------------
    def Iniciar(self):

#----------------------

        try:
            #***************** funções: ******************
            def close():
                if self.event == sg.WIN_CLOSED:
                    exit()#-------------fechar toda a aplicação python
            #*********************************************
        except Exception as error:
            print(f'Erro 02\n{error}')

#-------------------------------------------03--------------------------------------
        while True:
            self.event, self.values = self.janela.Read()
            close()
            
            #**************** vinculação: ****************
            if self.event == 'botao_L_externo':
                L_externo = Tela1()
                L_externo.Iniciar()  
            elif self.event == 'botao_L_interno':
                L_externo = Tela2()
                L_externo.Iniciar()
    
tela = Tela()
tela.Iniciar()