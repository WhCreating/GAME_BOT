from InquirerPy import inquirer
import random


def bot_kamen() -> str:
    rand = ['Камень', 'Ножницы', 'Бумага']
    otv = random.choice(rand)
    return otv



def kamen_noj():

    bot_kamens = bot_kamen()

    promt = inquirer.select(

        message="Что вы поставите?",
        choices=['Камень', 'Ножницы', 'Бумага']

    ).execute()

    if promt == 'Камень':
        if bot_kamens == 'Камень':
            print('Ничья')
        elif bot_kamens == 'Бумага':
            print('Вы проиграли')
        elif bot_kamens == 'Ножницы' :
            print('Вы выиграли')
    elif promt == 'Ножницы':
        if bot_kamens == 'Бумага':
            print('Вы выиграли')
        elif bot_kamens == 'Ножницы':
            print('Ничья')
        elif bot_kamens == 'Камень':
            print('Вы проиграли')
    elif promt == 'Бумага':
        if bot_kamens == 'Камень':
            print('Вы выиграли')
        elif bot_kamens == 'Бумага':
            print('Ничья')
        elif bot_kamens == 'Ножницы' :
            print('Вы проиграли')



    print(bot_kamens)





if __name__ == '__main__':
    kamen_noj()