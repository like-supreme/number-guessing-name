import random 
from art import logo 

computer_choose = 0

def ran_number(): #bilgisayarın rastgele sayı üretmesi sorunsuz çalışıyor
    computer_choose = random.randint(0,100)
    return computer_choose




def compare(): # compare sorunsuz çalışıyor
    player_number = int(input("Make a guess: " + ""))
    if player_number < computer_choose:
        print("too low")
        return player_number , computer_choose
    elif player_number > computer_choose:
        print("too high")
        return player_number , computer_choose
    elif player_number == computer_choose:
        print(f"You guessed right the answer is: {computer_choose}")
        return player_number , computer_choose
    else:
        print("Invalid input")
        return None
  

def game():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        life = 10        
    elif difficulty == "hard":
        life = 5
    else:
        print("Invalid input...")
        return None
    #print(f"You have {life} attempts to guess the number")
    while life > 0:
        print(f"You have {life} attempts to guess the number")
        guess , answer = compare()
        if guess == answer:
            print("You guessed right")
            print(f"Correct number was {answer}")
            break
        else:
            life -= 1
            if life == 0:
                print("You run out of lives \n You Loose. ")
                print(f"The correct number was {answer}")


is_game_on = True
while is_game_on:
    wanna_play = input("Would you like to play a game ? y/n ")
    
    computer_choose = ran_number() #diğer fonksiyonlarda kullanabilmek için. 
    #print(computer_choose)
    if wanna_play == "y":    
        print(logo)
        print( "Welcome to the Number Guessing Game")
        print("I'm thinking of a number between 1 and 100")
        game()
    elif wanna_play == "n":
        print("Goodbye")
        is_game_on = False
    else:
        print("Invalid input. restart the game")
        is_game_on = False

# en son problemimiz ise oyunun rastgele bir sayı vermesi ve o sayıdan başka sayı seçmemesi
#sebebi: global scope da tanımlı... 














