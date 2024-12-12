from InquirerPy import inquirer
import random


def bot_kamen() -> str:
    rand = ['Камень', 'Ножницы', 'Бумага']
    otv = random.choice(rand)
    return otv



def kamen_noj():
    promt = inquirer.select(

        message="Что вы поставите?",
        choices=['Камень', 'Ножницы', 'Бумага']

    ).execute()

    if promt == bot_kamen():
        print('Ничья')
    elif promt == 'Камень':
        if bot_kamen() == 'Бумага':
            print('Вы проиграли')
            print(bot_kamen())
        else :
            print('Вы выиграли')
            print(bot_kamen())
    elif promt == 'Ножницы':
        if bot_kamen() == 'Бумага':
            print('Вы выиграли')
            print(bot_kamen())
        else :
            print('Вы проиграли')
            print(bot_kamen())
    elif promt == 'Бумага':
        if bot_kamen() == 'Камень':
            print('Вы выиграли')
            print(bot_kamen())
        else :
            print('Вы проиграли')
            print(bot_kamen())






if __name__ == '__main__':
    kamen_noj()