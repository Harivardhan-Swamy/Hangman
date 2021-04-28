from words import word_list
import random


def get_word():
    word=random.choice(word_list)
    return word.upper()

def display_fig(tries):
    stages=["""

                                _________
                                |        |                
                                |        O
                                |       \\|/
                                |        |
                                |        /\\
                                |         
                                |
                            __________ 


    """,
    """

                                _________
                                |        |                
                                |        O
                                |       \\|/
                                |        |
                                |        /
                                |         
                                |
                            __________ 


    """,
    """

                                _________
                                |        |                
                                |        O
                                |       \\|/
                                |        |
                                |          
                                |         
                                |
                            __________ 


    """,
    """

                                _________
                                |        |                
                                |        O
                                |        |/
                                |        |
                                |          
                                |         
                                |
                            __________ 


    """,
    """

                                _________
                                |        |                
                                |        O
                                |        |
                                |        |
                                |          
                                |         
                                |
                            __________ 


    """,
    """

                                _________
                                |        |                
                                |        O
                                |        
                                |          
                                |          
                                |         
                                |
                            __________ 


    """,
    """

                                _________
                                |        |                
                                |          
                                |        
                                |         
                                |          
                                |         
                                |
                            __________ 


    """,
    """

                                
                                |                      
                                |          
                                |        
                                |          
                                |          
                                |         
                                |
                            __________ 


    """]
    return stages[tries-1]

def play(word):
    word_completion = '_' * len(word)
    tries = 8
    guessed_words = []
    guessed_letters = []
    guessed = False

    print("""#Welcome to hangman!!
             #You have 8 tries to geuss the movie
             #Geuss by whole name or an individual letter""")
    
    
    print(display_fig(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        entered=input("please enter a word or letter: ").upper()
        if (len(entered) == 1 and entered.isalpha()):
            if (entered in guessed_letters) :
                print("You already guessed that letter")
            elif (entered not in word) :
                print("The letter " + entered + "is not in the words") 
                tries-=1
                guessed_letters.append(entered)
            else:
                print("The letter",entered, "is in the word!!")
                guessed_letters.append(entered)
                word_as_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter == entered ]
                for index in indices :
                    word_as_list[index] = entered
                word_completion = "".join(word_as_list)
                if ("_" not in word_completion ):
                    guessed=True

        elif (len(entered) == len(word) and entered.isalpha()):
            if entered in guessed_words:
                print("You have already guessed the word!")
                    
            elif entered==word :
                print("Congrats the word ", entered , " is correct!")
                guessed =True
                word_completion=word
            
            elif entered!= word:
                print(entered ," is not the word")
                tries-=1
                guessed_words.append(entered)

        else :
            print("Not a valid guess :(")
            tries-= 1
        
        print(display_fig(tries))
        print("\n")
        print(word_completion)
        print('\n')

    if guessed:
        print("Congrats you  guessed the word!!")
    else:
        print("""Sorry you ran out of tries....
                 The word was """,word)

def main():
    word=get_word()
    play(word)
    while input("play agin [Y]es or [N]o : ").upper() == 'Y' :
        word=get_word()
        play(word)
    
if __name__ == "__main__":
    main()
    

