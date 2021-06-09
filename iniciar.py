import PySimpleGUI as sg
import layouts
from calc_imc import CalculaIMC


def isnumber(num):
    try:
        float(num)
        # Se verdadeiro retorna True
        return True
    except:
        pass
    # Caso contrário retorna False
    return False



sg.theme('Reddit')
layout = layouts.layout_principal()

# -- Iniciando o programa
window = sg.Window("IMC", layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break

    # -- Escreve o valor do IMC na tela
    def write_imc():
        window['status_imc'].update(f"IMC: {objimc.imc}", visible=True)

    # -- Limpa os campos de preenchimento
    def clear_values():
        window['altura'].update("")
        window['kilo'].update("")


    if event == 'Calcular':
        if isnumber(value['altura']) and isnumber(value['kilo']):
            objimc = CalculaIMC(float(value['kilo']), float(value['altura']))

            if objimc.status_peso == 0:
                window['status_peso'].update("Abaixo do peso", visible=True, text_color="yellow")
                write_imc()
                clear_values()
            elif objimc.status_peso == 1:
                window['status_peso'].update("Peso normal", visible=True, text_color="green")
                write_imc()
                clear_values()
            elif objimc.status_peso == 2:
                window['status_peso'].update("Sobrepeso", visible=True, text_color="red")
                write_imc()
                clear_values()
            elif objimc.status_peso == 3:
                window['status_peso'].update("Obesidade Grau 1", visible=True, text_color="red")
                write_imc()
                clear_values()
            elif objimc.status_peso == 4:
                window['status_peso'].update("Obesidade Grau 2", visible=True, text_color="red")
                write_imc()
                clear_values()
            elif objimc.status_peso == 5:
                window['status_peso'].update("Obesidade Grau 3", visible=True, text_color="red")
                write_imc()
                clear_values()

        else:
            layouts.pop_up_value_error()
            clear_values()
window.close()
