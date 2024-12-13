from InquirerPy import inquirer
from colorama import init, Fore, Back, Style
import os
from choice_num import *
from kamen_nojnicy import *

os.system('cls||clear')


init()

def console_picture():
    print(Style.BRIGHT + Fore.YELLOW)
    with open('./logo.txt', 'r') as f:
        print(f.read())
console_picture()


confirm = inquirer.confirm(message="Confirm?(ru/en)").execute()
os.system('cls||clear')

def page_game1(setts):
    if setts == "Играть":
        os.system('cls||clear')

        settin = inquirer.select(
            message="Выберите сложность игры.",
            choices=["Easy", "Middle", "Hard"],
        ).execute()

        if settin == 'Easy':
            main_game1('Easy')
        elif settin == 'Middle':
            main_game1('Middle')
        elif settin == 'Hard':
            main_game1('Hard')

    choices = inquirer.select(
        message="",
        choices=["Вернуться в меню"],
    ).execute()


    os.system('cls||clear')
    return page_menu()

def page_game2(setts):
    if setts == "Играть":
        os.system('cls||clear')

        kamen_noj()

    choices = inquirer.select(
        message="",
        choices=["Вернуться в меню"],
    ).execute()


    os.system('cls||clear')
    return page_menu()

def page_menu():
    if confirm is True:
        choices = inquirer.select(
            message="Выберите игру:",
            choices=["Угадай число", "Камень, ножницы, бумага","Выход"],
        ).execute()
        os.system('cls||clear')

        if choices == 'Угадай число':
            settings = inquirer.select(
                message="Угадай число.",
                choices=["Играть", "Назад"],
            ).execute()
            os.system('cls||clear')
            if settings == 'Играть':
                return page_game1(settings)
            else :
                return page_menu()
        elif choices == 'Камень, ножницы, бумага':
            settings = inquirer.select(
                message="Камень, ножницы, бумага",
                choices=["Играть", "Назад"],
            ).execute()

            os.system('cls||clear')

            if settings == 'Играть':
                return page_game2(settings)
            else :
                return page_menu()

        else :
            print('Выход...')
    else :

        choices = inquirer.select(
            message="Select a game:",
            choices=["Guess the number", "Rock, paper, scissors", "Exit"],
        ).execute()
        os.system('cls||clear')

        if choices == 'Guess the number':
            settings = inquirer.select(
                message="Guess the number",
                choices=["Играть","Back"],
            ).execute()
            os.system('cls||clear')

            if settings == 'Играть':
                return page_game1(settings)
            else :
                return page_menu()
        elif choices == 'Rock, paper, scissors':
            settings = inquirer.select(
                message="Rock, paper, scissors",
                choices=["Играть", "Back"],
            ).execute()
            os.system('cls||clear')
            if settings == 'Играть':
                return page_game2(settings)
            else :
                return page_menu()

        else:
            print('Exit...')

if __name__ == '__main__':
    page_menu()