import random

def games(atts, len, rand):
    if len == 'ru':
        num = random.randint(1, rand)
        att = 0
        while att < atts:
            otv = int(input(f'Угадай число от 1 до {rand} ({atts} попытки): '))
            if otv == num:
                print('Win!!!')
                break

            if att == atts:
                print('Fail')
                break
            if otv > num:
                print('Загаданное число меньше.')
            elif otv < num:
                print('Загаданное число больше.')
            att+=1
    else :
        num = random.randint(1, rand)
        att = 0
        while att < atts:
            otv = int(input(f'Guess a number from 1 to {rand} ({atts} attempts): '))
            if otv == num:
                print('Win!!!')
                break

            if att == atts:
                print('Fail')
                break
            if otv > num:
                print('The hidden number is smaller.')
            elif otv < num:
                print('The hidden number is greater.')
            att += 1



def main_game1(a):
    if a == 'Easy':
        games(3, 'ru', 10)

    elif a == 'Middle':
        games(10, 'ru', 50)

    elif a == 'Hard':
        games(20, 'ru', 100)


if __name__ == '__main__':
    main_game1('Hard')