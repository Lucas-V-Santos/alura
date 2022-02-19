from builtins import set
import random

def play():

    print_opening_file()
    secret_word = load_secret_word()
    correct_letters = inicialize_correct_letters(secret_word)

    hanged = False
    got_in_right = False
    errors = 0

    print("A Sombra da Palavra Secreta é: \n {} \n com {} letras".format(correct_letters, len(correct_letters)))

    while(not hanged and not got_in_right):
        guess = ask_for_guess()
        if(guess in secret_word):
            mark_correct_letter(secret_word, guess, correct_letters)
        else:
            errors += 1
        hanged = errors == 6
        got_in_right = "_" not in correct_letters

        print(correct_letters)
        if(guess in secret_word):
            print("Você acertou! Restam {} tentativas para acertar {} letras.".format((6-errors), correct_letters.count("_")))
        else:
            print("Você acertou! Restam {} tentativas para acertar {} letras.".format((6 - errors), correct_letters.count("_")))

    if(got_in_right):
        print_winner_message()
    else:
        print_loser_message()

def print_opening_file():
    print("**********************************")
    print("   Welcome to the Hanged Game   ")
    print("**********************************")

def load_secret_word():
    archieve = open("palavras.txt", "r")
    words = []
    for line in archieve:
        line = line.strip()
        words.append(line)
    archieve.close()
    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word

def inicialize_correct_letters(secret_word):
    correct_letters = ["_" for letter in secret_word]
    return correct_letters

def ask_for_guess():
    guess = input("Enter your guess here: ")
    return guess.strip().upper()

def mark_correct_letter(secret_word, guess, correct_letters):
    index = 0
    for letter in secret_word:
        if (letter == guess):
            correct_letters[index] = guess.upper()
        index += 1
def print_winner_message():
    print("Aí sim! Você venceu o jogo. :)")

def print_loser_message():
    print("Ahh! Mais sorte da próxima vez. :(")

if(__name__ == "__main__"):
    play()