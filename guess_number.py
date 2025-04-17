from random import randint

number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    guess = int(input())

    if guess > number:
        print('Ваше число больше загаданного')

    elif guess < number:
        print('Ваше число меньше загаданного')
    else:
        print('Ура! Вы угадали!')
        break