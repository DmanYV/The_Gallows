import random


def hangman():
    words = [
        "Яблоко",
        "Солнце",
        "Кофе",
        "Море",
        "Дом",
        "Книга",
        "Цветок",
        "Музыка",
        "Счастье",
        "Путешествие",
        "Велосипед",
        "Звезда",
        "Чай",
        "Радуга",
        "Луна",
        "Кошка",
        "Дружба",
        "Вода",
        "Парк",
        "Улыбка"
    ]
    random_words = random.choice(words)
    wrong = 0
    stages = ["",
              "___________        ",
              "|         |        ",
              "|         |        ",
              "|         O        ",
              "|        /|\\       ",
              "|        / \\       ",
              "|                  "
              ]
    rletters = list(random_words)
    board = ["_"] * len(random_words)
    win = False
    print('Добро пожаловать на казнь!')

    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Введите букву: '
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print('\n'.join(stages[0: e]))
        if '_' not in board:
            print('Вы выиграли! Было загадано слово: ')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print('Вы проиграли! Было загадано слово: {}.'.format(random_words))


if __name__ == '__main__':
    hangman()
