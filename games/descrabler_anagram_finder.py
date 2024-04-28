#--------------------------------
#  please excuse my trash code
#--------------------------------

import os
from nltk.corpus import words
word_list = words.words()


title = """
-----------------------------------------------------------------------------------
 ________ _            _____                                     _     _           
 |__   __| |          |  __ \                                   | |   | |          
    | |  | |__   ___  | |  | | ___  ___  ___ _ __ __ _ _ __ ___ | |__ | | ___ _ __ 
    | |  | '_ \ / _ \ | |  | |/ _ \/ __|/ __| '__/ _` | '_ ` _ \| '_ \| |/ _ \ '__|
    | |  | | | |  __/ | |__| |  __/\__ \ (__| | | (_| | | | | | | |_) | |  __/ |   
    |_|  |_| |_|\___| |_____/ \___||___/\___|_|  \__,_|_| |_| |_|_.__/|_|\___|_|
-----------------------------------------------------------------------------------
                                                                                   """                                                  
def load_title():
   os.system("cls")
   print(title)
   print("You can Also Use This To Find Anagrams\n")
   print("-----------------------------------------------------------------------------------")


def add_word():
   word_list_length = len(word_list)
   print(f"TOTAL WORDS: {word_list_length}")
   print("Please Enter The Word You Would Like To Add\n MAKE SURE YOU SPELL IT RIGHT")
   add_word = input("#")
   word_list.append(add_word)

def descramble(given_word):
    gw_chars = []
    test_word = ""
    test_word_chars = []
    test_word_correct = False
    #divide given word into individual characters
    for char in given_word:
        gw_chars.append(char)
    #print(gw_chars)

    #divides words into individual chars
    for item in word_list:
        test_word_chars.clear()
        test_word = item
        #print(test_word)
        for char in test_word:
            test_word_chars.append(char)
    #checks if test word and given word are same length and letters
        if len(test_word_chars) == len(gw_chars):
            
            for item in gw_chars:
                if item in test_word_chars:
                    test_word_chars.remove(item)
                else:
                    #print("the letters dont match")
                    pass
                    
            if len(test_word_chars) == 0:
                print(f"This Is Your Word Unscrambled: {test_word} ")
                
        else:
            #print("the word is too short or long")
            pass
    cont = input("Press ENTER To Continue")

#app loop
running = True
while running == True:
   os.system("color 3")
   load_title()
   print("Enter A Number To Select An Option\n")
   print("1. Descramble A Word")
   print("2. Add Words To The List")
   print("3. Close")
   user_option = input("#")


   if user_option == "1":
     load_title()
     print("Please Enter The Scrambled Word")
     scrambled_word = input("#")
     descramble(scrambled_word)
   elif user_option == "2":
     load_title()
     add_word()
   elif user_option == "3":
     quit()


    
    

    
    
