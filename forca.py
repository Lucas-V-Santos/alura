from builtins import set


def play():
    print("**********************************")
    print("   Welcome to the Hanged Game   ")
    print("**********************************")

    secret_word  = "maça".upper()
    correct_letters = ["_" for letter in secret_word]
    hanged = False
    got_in_right = False
    errors = 0

    print(correct_letters)

    while(not hanged and not got_in_right):
        guess = input("Enter your guess here: ")
        guess = guess.strip().upper()
        if(guess in secret_word):
            index = 0
            for letter in secret_word:
                if(letter == guess):
                    #print("{} was fouund in position {}".format(guess, (index+1)))
                    correct_letters[index] = guess.upper()
                index += 1
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
        print(":) Você Venceu o Jogo!")
    else:
        print(":( Boa Sorte na Próxima!")
    print("Fim do Jogo")

if(__name__ == "__main__"):
    play()