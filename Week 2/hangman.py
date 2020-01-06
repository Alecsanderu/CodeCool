import time
from timeit import default_timer as timer
import random
import datetime

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/          ''')
print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')

start = timer()
name = input("What is your name? ")
if name.lower() == 'exit':
    exit()
print("Hello, " + name, "! It's time to play The Hangman Game!")
print("Rules:")
print("Guess the word by entering one letter at a time or try guessing the whole word.")
print("If you enter the whole word and you get it wrong, you lose!")
print("\n")


while name.lower != "exit":
    guesses = ''
    lives = 8
    used = []
    wrong = 0
    with open('capitals_and_countries.txt') as myfile:
        lines = [line for line in myfile]
        rand_line = random.randint(0, 11)
        capital = lines[rand_line].split("|")[1]
        capital = capital[: -1]
        country = lines[rand_line].split("|")[0]
    dat = datetime.datetime.now()
    date = dat.strftime("%x")
    time.sleep(1)

    hangman = (

        """
    _________
        |/        
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        """,

        """
    _________
        |/   |      
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        H""",

        """
    _________       
        |/   |              
        |   (_)
        |                         
        |                       
        |                         
        |                          
        |___                       
        HA""",

        """
    ________               
        |/   |                   
        |   (_)                  
        |    |                     
        |    |                    
        |                           
        |                            
        |___                    
        HAN""",


        """
    _________             
        |/   |               
        |   (_)                   
        |   /|                     
        |    |                    
        |                        
        |                          
        |___                          
        HANG""",


        """
    _________              
        |/   |                     
        |   (_)                     
        |   /|\                    
        |    |                       
        |                             
        |                            
        |___                          
        HANGM""",



        """
    ________                   
        |/   |                         
        |   (_)                      
        |   /|\                             
        |    |                          
        |   /                            
        |                                  
        |___                              
        HANGMA""",


        """
    ________
        |/   |     
        |   (_)    
        |   /|\           
        |    |        
        |   / \        
        |               
        |___           
        HANGMAN""")

    while lives > 0:

        failed = 0   
        for char in capital:      
            if char.upper() in guesses.upper():    
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1 
        if failed == 0 or guesses.upper() == capital.upper():        
            end_time = timer()
            timp = end_time - start
            print("\n")
            print("You won!")
            print("It took you:", end=" ")
            print(int(timp), end=" ")
            print(" seconds to guess the capital!")
            tries = len(used)
            print("You tried " + str(tries) + " letters")
            score = (name + "| " + date + "| " + str(int(timp)) + " seconds| " + str(tries) + " tries| " + capital)
            print("Your score is: " + score)
            print("Do you want to play again?(yes/no)")
            answer = input("")
            while answer != "yes" and answer != "no":
                print("Please enter 'yes' or 'no'!") 
                answer = input("")
            if answer == "yes":
                break
            elif answer == "no":
                score = (name + "| " + date + "| " + str(int(timp)) + " seconds| " + str(tries) + " tries| " + capital)
                print("Your score is: " + score)
                hiscc = open("highscore.txt", "a")
                hiscc.write("\n")
                hiscc.write(str(score))
                hiscc.write("\n")
                hiscc.close()
                hisc = open("highscore.txt", "r")
                print("Other players:")
                for line in hisc:
                    print(line)
                hisc.close()
                exit()
        print("\n") 
        print("So far you used:", end=" ")
        print(*used)
        guess = input("Guess a character:")
        print("\n") 
        used.append(guess)
        guesses += guess.upper()   
        if guess.lower() == "exit":
            exit()   
        if len(guess.upper()) > 1:
            if guess.upper() != capital.upper():
                lives -= 2

        if guess.upper() not in capital.upper():  
            lives -= 1  
            print(hangman[wrong])
            wrong += 1
            print("\n")
            print("You have ", + lives, 'lives left') 
            print("\n")
            if lives <= 0:
                end_time = timer()
                timp = end_time - start
                print("Game Over!")
                print("Your word is " + str(capital) + "!")
                print("You played for: ", end=" ")
                print(int(timp), end=" ")
                print("seconds!")
                tries = len(used)
                print("You tried " + str(tries) + " letters")
            if lives == 1:
                print("Hint: The capital of " + str(country) + "!")
            
           
                




