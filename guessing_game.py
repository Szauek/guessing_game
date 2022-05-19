from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0


def check_answer(guess, answer, turns):
    if guess > answer:
        print('Za duza')
        return turns - 1
    elif guess < answer:
        print('Za niska')
        return turns - 1
    else:
        print(f"Udalo sie, prawidłowa liczba to {answer}")


def set_difficulty():
    level = input("Wybierz poziom trudnosci. 'latwy' lub 'trudny':")
    if level == "latwy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Witaj w grze zgadnij numer")
    print("Odgadnij nr pomiedzy 1-100")
    answer = randint(1, 100)

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        guess = int(input("Podaj liczbe: "))
        print(f'Masz {turns} prob do odgadniecia numeru.')

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('Przegrales')
            return
        elif guess != answer:
            print('Sprobuj ponownie')


game()
