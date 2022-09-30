import PySimpleGUI as sg # Importação da ferramenta PySimpleGUI, após o comando "as" podemos definir o apelido "sg" para que seja mais rápido e facil usar a biblioteca
import pandas as pd #Importação da ferramenta Pandas, definindo o apelido "pd"

str

sg.theme('LightGreen1') # Aqui definimos o tema que será usado no layout

class First(): # Criação da classe
    def fun_matricula(): # Criação da função
        layout_cadastro = [ # Criação da tela, especificando tamanho, fonte e KEY que é fundamental para o funcionamento do programa
            [sg.Text('Nome', font=('Arial', 20)),sg.Input('', font=('Arial', 20), key='-NOME-')],
            [sg.Text('Atuação', size=(10), font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-TIME-'),
            sg.Text('Valor/hora', size=(10), font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-CUSTO-')],
            [sg.Button('INICIAR', expand_x=True, font=('Arial', 20), key='-INICIAR-')]
        ]
        return sg.Window('Cadastro', layout=layout_cadastro, margins=(10, 10), finalize=True) # Aqui estamos criando o comando para que a janela seja criada quando a função for executada

    matricula = fun_matricula() # Aqui estamos definindo a variavel "matricula" como respondavel pelo funcionamento da função "fun_matricula"


class cliente():
    def reg_cliente():
        layout_cad_client = [ 
            [sg.Text('Cliente', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-CONTRATANTE-')]
        ]
        return sg.Window('CLIENTE', layout=layout_cad_client, margins=(10,10), finalize=True)

    Cad_Cliente = reg_cliente()

 
while True:
    '''
    usar a funcao .hide para esconder as janelas e alterar entre elas 
    o while true so opera nessa cituação
    window, event, Value
    '''
