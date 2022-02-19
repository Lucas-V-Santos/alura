import forca
import adivinhacao

def choose_game():
    print("**********************************")
    print("   Welcome to the Hanged Game   ")
    print("**********************************")

    print("(1) Forca, (2) Adivinhação")

    game = int(input("Enter your choice here:"))

    if(game == 1):
        print("Você escolheo jogar FORCA")
        forca.play()
    elif(game == 2):
        print("Você escolheu jogar ADIVINHAÇÃO")
        adivinhacao.play()

if (__name__ == "__main__"):
    choose_game()