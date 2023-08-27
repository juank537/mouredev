# Juego de Piedra, Papel o Tijera (CÓDIGO TOMADO DE UNA PÁGINA)

import random 
from enum import IntEnum

class Action(IntEnum):
    Piedra = 0
    Papel = 1
    Tijeras = 2

count_user = 0
count_pc = 0
count_plays = 0

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Seleccione una opción ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"{user_action.name} vs {computer_action.name}. ¡ES UN EMPATE!")
    elif user_action == Action.Piedra:
        if computer_action == Action.Tijeras:
            print("¡La piedra aplasta las tijeras! ¡HAS GANADO!")
        else:
            print("¡El papel cubre a la piedra! ¡HAS PERDIDO!")
    elif user_action == Action.Papel:
        if computer_action == Action.Piedra:
            print("¡El papel cubre a la piedra! ¡HAS GANADO!")
        else:
            print("¡Las tijeras cortan el papel! ¡HAS PERDIDO!")
    elif user_action == Action.Tijeras:
        if computer_action == Action.Papel:
            print("¡Las tijeras cortan el papel! ¡HAS GANADO!")
        else:
            print("¡La piedra aplasta las tijeras! ¡HAS PERDIDO!")

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Selección incorrecta. Seleccione uno de los valores siguientes {range_str}")
        continue

    computer_action = get_computer_selection()
    count_plays += 1
    determine_winner(user_action, computer_action)
    print(f'Jugadas: {count_plays}')
    play_again = input("¿Jugamos de nuevo? (s/n): ")
    if play_again.lower() != "s":
        break


