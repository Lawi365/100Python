#THIS IS PART OF THE 100 PYTHON CHALLENGE
# MY DAY 1 IMPLEMENTATION OF HANGMAN
#AUTHOR MBOYA LAWRENCE.
#FEEL FREE TO MODIFY
#FLOW CHART.

import random
words ="The most basic data structure in Python is the sequence \
         Each element of a sequence is assigned a number \
         its position or index The first index is zero the second index is one and so forth\
         Python has six built in types of sequences but the most common ones are lists \
         and tuples which we would see in this tutorial\
         There are certain things you can do with all sequence types\
         These operations include indexing slicing adding multiplying\
         and checking for membership In addition Python has builtin functions\
         for finding the length of a sequence and for finding its largest and smallest elements"
         
words=words.lower().split(' ')
life = 6
hangmanlist = ['''
            +---+
            |   |
            o   |
           /|\  |
           / \  |
                |
         ========       
            '''
            ,
            '''
    YOU OPENED THE DUNGEON
            +---+
            |   |
            |   |
            o   |
           /|\  |
           / \  |
        =\     /=
        '''      ,
            '''
     YOU HAVE RELEASED THE ROPE
            +---+
            |   |
            |   |
            o   |
           /|\  |
           / \  |
        =\     /=
        ^^^^^^^^^          
        '''
                ,
            '''
            +---+
            |   |
            |   |
            o   |
           /|\  |
        =\     /=
          00000  
        ^^^^^^^^^         
        ''',
            '''
            +---+
            |   |
            |   |
            |   |
            o   |
        =\ /|\ /=
         00\00/00  
       ^^^^^^^^^^               
        '''
                ,
            '''
            +---+
            |   |
            |   |
                |
                |
      ++++(- -)++++
            .
       ILL BE BACK
    IN THE END HE WAS SAVED        
        ''']

# 1. Get random word
random_word = words[random.randint(0,len(words))]

# 2. GENERATE -- EQUIVALENT TO WORD LENGTH.
dash =list( '-'*len(random_word) )
print(''.join(dash))

while True:
    welcome= '....Welcome to Hangman....'
    #3. GUESS THE LETTER.
    user_guess = input(str('Enter Letter: '))
    # print('Your guess is : ', user_guess)

    #4.CHECK IF LETTER IN PART OF THE WORD.
    if user_guess in random_word:
        #get the index of word the print it
        for i in range(len(random_word)):
            if random_word[i] == user_guess:
                dash[i]=user_guess
                print(''.join(dash))
            #if the dict'ionary is equal to my original word 
        if ''.join(dash) == random_word:
            print("The word is {}".format(random_word))
            print("You Win")
            break
        
    else:
        #DECREASE LIFE BY 1 THEN CONTINUE WITH THE LOOP
        print(hangmanlist[abs(life-6)])
        life -= 1
        print("\a \aRemaining Attempts: ",life)
        # if life < 5:
        #     print("Hint: {}".format(random_word[random.randint(1,len(random_word))]))
        if life == 0 :
            print("GAME OVER \n The word was: '{}'".format(random_word))
            break
