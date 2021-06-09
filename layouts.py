import PySimpleGUI as sg

def layout_principal():
    # -- Parâmetros padrões
    DEFAULT_PAD=(10,10)
    DEFAULT_TEXT_SIZE=(20,1)
    DEFAULT_INPUT_SIZE=(5,1)


    layout_tela = [
        #  -- Título
        [sg.Text("CALCULO DE IMC",
            size=DEFAULT_TEXT_SIZE,
            justification='center',
            font=20)
        ],


        # -- Input do usuário
        [sg.Text("Altura (em Centrímetros):", size=DEFAULT_TEXT_SIZE),
            sg.Input(size=DEFAULT_INPUT_SIZE,
            key='altura',
            justification='center',
            tooltip='Insira sua Altura em Centrímetros')
        ],

        [sg.Text("Peso (em Kilos):", size=DEFAULT_TEXT_SIZE),
            sg.Input(size=DEFAULT_INPUT_SIZE,
            key='kilo',
            justification='center',
            tooltip='Insira seu peso em Kilos')
        ],


        # -- Resposta ao usuário
        [sg.Text(
            key='status_peso',
            size=DEFAULT_TEXT_SIZE,
            font=10,
            visible=False,
            justification='center',
            pad=DEFAULT_PAD
        )],

        [sg.Text(
            key='status_imc',
            size=DEFAULT_TEXT_SIZE,
            font=10,
            visible=False,
            justification='center',
            pad=DEFAULT_PAD
        )],

        # -- Botão de interação
        [sg.Button('Calcular')]
    ]

    return layout_tela


def pop_up_value_error():
    return sg.popup_ok('Valores inválidos, por favor, digite apenas números')
