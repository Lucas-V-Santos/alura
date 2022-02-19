import random

def play():

    print("**********************************")
    print("   Welcome to the Guessing Game   ")
    print("**********************************")


    secret_number = random.randrange(1,101)
    attempts_counter = 3
    round_counter = 1
    difficulty_level = 1
    guess_points = 1000



    print("You have to define a difficulty level:")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    difficulty_level_choice = int(input("Enter your choice here: "))

    if(difficulty_level_choice == 1):
        attempts_counter = 3
    elif(difficulty_level_choice == 2):
        difficulty_level = 2
    else:
        attempts_counter = 1




    while(round_counter <= attempts_counter):
        print("Attempt {} de {} ".format(round_counter, attempts_counter))
        guess_str = input("Please, enter your guess (it must be between 1 and 100):")
        print("You entered: ", guess_str)
        guess_int = int(guess_str)

        if(guess_int < 1 or guess_int >100):
            print("Please enter a number between 1 and 100")
            continue

        hit = guess_int == secret_number
        major_mistake = guess_int > secret_number
        minor_mistake = guess_int < secret_number

        if (hit):
            print("Correct!")
            break
        else:
            if(major_mistake):
                guess_points = guess_points - abs((guess_int - secret_number))
                print("Major")
            elif(minor_mistake):
                guess_points = guess_points - abs((guess_int - secret_number))
                print("Minor")
        round_counter = round_counter + 1
    print("Secret Number Was: {}".format(secret_number))
    print("Fim do Jogo! Sua pontuação final é: {}".format(guess_points))

if(__name__ == "__main__"):
    play()