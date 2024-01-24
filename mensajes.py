import pyautogui as pg
import pyperclip as pyc
import time

emojis = '🌸💖🌺😻🌹😍🌻🥰🌷❤️'
emojis2 = '😎🤨😡🥵'
mensajito = "Soy un bot "

def dibujar_corazon(e):
    c = [
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    ]

    corazon = ''

    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] == 1:
                corazon += e
            else:
                corazon += '   '
        corazon += '\n'

    pyc.copy(corazon)

def poner_mensaje(x):
    global mensajito
    mensajito = mensajito[:-1] + x  # Reemplaza el último emoji con el nuevo
    pyc.copy(mensajito)

mensajes = int(input('Número de mensajes: '))
time.sleep(3)

for i in range(mensajes):
    #dibujar_corazon(emojis[i % 10])
    poner_mensaje(emojis2[i % 4])
    pg.hotkey('ctrl', 'v')
    #time.sleep(1)  # Añadir una pausa después de pegar
    #print("Ya pegue el mensaje")
    pg.press('enter')
    #time.sleep(1)  # Añadir una pausa después de presionar 'enter'
