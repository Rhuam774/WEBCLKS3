#RHUAM PFC
#webcrawler_LINKS                         #--/--/---
#------------------------------------------------------------

from os import system
import re
import requests
import PySimpleGUI as sg

def L():
    try:
        system("clear")
    except:
        None
def lg():
    print('\n*******************************webC2******************************\n')
class Tela2:

#======================================= tela: ===========================================
    def __init__(self):
        layout = [
            [sg.T("**************************************************************webC2*************************************************************\n")],
            [sg.T('URL: '), sg.Input('https://',key=('url'))],
            [sg.Checkbox('Encontrar possiveis diretorios da pagina',key=('Enc_diretorios'))],  #encontrar diretorios
            [sg.Checkbox('Encontrar subdominios e links contidos na paginas', key=('Enc_subdominios'))],
            [sg.Output(size=(90, 15),key=('output'))],######################## testar o key do output*
            [sg.Button('buscar')]
        ]
        self.janela = sg.Window('webC_LKS2-interno.py').layout(layout)

#======================================= organização da tela: ===========================================
    def Iniciar(self):
            
            while True:
                self.event, self.values = self.janela.Read()

                try:#++++++++++++++++++++++++++++++++++++++++++++-01  
                    if self.event == sg.WIN_CLOSED:
                        break

                #--------------------------------------------------
                    url01 = self.values['url']
                    Enc_diretorios = self.values['Enc_diretorios']
                    Enc_subdominios = self.values['Enc_subdominios']
                    #Output = self.values['output']
                    #--------------------------------------------------
                    
        #======================================= funções: ===========================================
                    def filLINKS(links):
                        links = str(links)
                        fil_links1 = links.replace("'", "")
                        fil_links2 = fil_links1.replace("[", "")
                        fil_links3 = fil_links2.replace("]", "")
                        fil_links4 = fil_links3.replace(",", "\n")
                        fil_links5 = fil_links4.replace(" ", "")
                        texto_links.write(fil_links5+'\n') 
                        print(fil_links5)

                    if self.event == sg.WIN_CLOSED:
                        break
                    pagina = requests.get(url01).text
                    arquivo = open("texto.txt","w+")
                    arquivo.write(pagina)
                    arquivo.close()
                    texto = open("texto.txt","r")
                    texto_links = open("links1.txt", "w")
                    
                    try:#++++++++++++++++++++++++++++++++++++++++++++-02
                        if Enc_diretorios == True:
                            print('\n==============================================================================')
                            print(f'***** Possiveis diretorios de "{url01}" encontrado na fonte da pagina de {url01}: *****\n')
                            for lin in texto:
                                links = re.findall(r"\w+\/[\w-]*.[\w\/-]*.\w+", lin)
                                if len(links) == 0:
                                    None
                                else:
                                    filLINKS(links)
                            print('\n==============================================================================')
                        elif Enc_subdominios:
                            print('\n==============================================================================')
                            print(f'*************************** Links encontrado na fonte da pagina de "{url01}": **************************\n')
                            for lin in texto:
                                links = re.findall(r"http[\w*://.-]+", lin)
                                if len(links) == 0:
                                    None
                                else:
                                    filLINKS(links)
                            print('\n==============================================================================')
                                    
                    except Exception as erro:
                        print('-----------------------------------------------------------------------------------')
                        print("\nerro 02\n")
                        print(f"Erro: {erro}")
                        print('-----------------------------------------------------------------------------------')
                        
                except Exception as erro:
                    print('-----------------------------------------------------------------------------------')
                    print("\nerro 01\n")
                    print(f"Erro: {erro}")
                    print('-----------------------------------------------------------------------------------')
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF