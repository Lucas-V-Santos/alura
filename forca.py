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
            print("Você acertou! Restam {} tentativas para acertar {} letras.".format((7 - errors),correct_letters.count("_")))
        else:
            errors += 1
            print("Você errou! Restam {} tentativas para acertar {} letras.".format((7 - errors),correct_letters.count("_")))
            draw_hang(errors)

        hanged = errors == 7
        got_in_right = "_" not in correct_letters

        print(correct_letters)


    if(got_in_right):
        print_winner_message()
    else:
        print_loser_message(secret_word)

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
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_loser_message(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def draw_hang(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

if(__name__ == "__main__"):
    play()