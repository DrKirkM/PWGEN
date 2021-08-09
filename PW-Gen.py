'''
@Author: KM

This program randomly generates passwords based on how strong or weak the 
user wants it to be. 

*********************************WARNING********************************************
The Python documentation warns that Python's built-in random number generator
isn't suitable for cryptographic purposes, where a minimum level of actual 
randomness is required to create random number generators to encrypt data 
with little risk of third-party decryption. If it's important to you that 
the list is truly random and unpredictable, such as for a raffle drawing, 
it's important to use the right random number generator.

This program is just an excercise in using python. 
************************************************************************************

'''
import random
import string

print("""
.______            _______  _______ .__   __.  _______ .______          ___   .___________.  ______   .______      
|   _  \          /  _____||   ____||  \ |  | |   ____||   _  \        /   \  |           | /  __  \  |   _  \     
|  |_)  |  ______|  |  __  |  |__   |   \|  | |  |__   |  |_)  |      /  ^  \ `---|  |----`|  |  |  | |  |_)  |    
|   ___/  |______|  | |_ | |   __|  |  . `  | |   __|  |      /      /  /_\  \    |  |     |  |  |  | |      /     
|  |             |  |__| | |  |____ |  |\   | |  |____ |  |\  \----./  _____  \   |  |     |  `--'  | |  |\  \----.
| _|              \______| |_______||__| \__| |_______|| _| `._____/__/     \__\  |__|      \______/  | _| `._____|
         """)

print('Welcome to the password generator!')

def really_strong(): #This is a function for producing randomly (as random as it gets for python at least) generated letters, numbers, and symbols 
    symbols = '!@#$%^&*,?().'
    strong_pass = ''.join([random.choice(symbols) + random.choice(string.ascii_letters + string.digits) for n in range(14)])
    finish = random.sample(strong_pass, len(strong_pass))
    complete = ''.join(finish)
    print(complete + '\n')

def strong():
    symbols = '!@#$%^&*(),?.'
    strong_pass = ''.join([random.choice(symbols) + random.choice(string.ascii_letters + string.digits) for n in range(8)])
    finish = random.sample(strong_pass, len(strong_pass))
    complete = ''.join(finish)
    print(complete + '\n')

def weak():
    strong_pass = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
    finish = random.sample(strong_pass, len(strong_pass))
    complete = ''.join(finish)
    print(complete + '\n')

def pwn():
    easy = ['123', 'password', '123456', 'password123', 'admin'] #hehehehehehehe
    why_would_you_do_this = random.choice(easy)
    print(why_would_you_do_this + '\n')

def menu(): #The menu
    while True:
        a = print("Please select the type of password to generate: \n 1. Really Strong \n 2. Strong \n 3. Weak\n 4. PLZ PWN ME\n 5. EXIT")
        menu_item_choice = input("Chose your menu item: " + str())
        
        if menu_item_choice == str(1):
            print("Here is your really strong password:  \n")
            really_strong()
            continue

        elif menu_item_choice == str(2):
            print("Here is your strong password:  \n")
            strong()
            continue

        elif menu_item_choice == str(3):
            print("Here is your weak password:  \n")
            weak()
            continue

        elif menu_item_choice == str(4):
            print("Here you go dummy:  \n")
            pwn()
            continue

        elif menu_item_choice == str(5):
            print("Exiting")
            break

        else:
            print("Invalid Choice! \n")
            continue
menu()