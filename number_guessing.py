import random
# sayıyı bilgisayar seçecek biz o sayıya yakınlaşmaya çalışacağız. 

def number_guessing_name():
    comp_number = random.randint(0,100)
    return comp_number

def compare(user_number , comp_number):
    if user_number < comp_number:
        return f"Your number {user_number} is smaller than computer number. try with higher numbers "
    elif user_number > comp_number:
        return f"Your number {user_number} is bigger than computer number. Try with lower numbers "
    elif user_number == comp_number:
        return "You guessed right. "
    else: 
        print("Invalid option please try again")
        return None
    return user_number , comp_number
    
#comp_number = number_guessing_name()

def main():
    comp_number = number_guessing_name()
    while True:
        user_number = int(input("Guess a number: "))
        if user_number == 0:
            break
        result = compare(user_number , comp_number)
        print(result)
        if user_number == comp_number:
            break
    
gameplay = True
while gameplay:
    cont = input("Want to play y/n ?")
    if cont == "y":
        main()
    elif cont == "n":
        break
    else: 
        print("Invalid option please try again")
        break
  







