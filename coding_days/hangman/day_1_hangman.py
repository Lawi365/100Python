#THIS IS PART OF THE 100 PYTHON CHALLENGE
# MY DAY 1 IMPLEMENTATION OF HANGMAN

#FLOW CHART.

import random
words = ["happy", "saddle","Hospital"]
welcome= '....Welcome to Hangman....'
life = 6


# 1. Get random word
random_word = words[random.randint(0,len(words)-1)]

# 2. GENERATE -- EQUIVALENT TO WORD LENGTH.
dash = '-'*len(random_word)
# print(dash)
print(welcome)

for i in range(len(random_word)+3):
      
    print(random_word)  
    # 3. ASK USER TO ENTER LETTER.
    user_entry = input(str('Enter Letter: '))
    
    print('your entry is :', user_entry)
     
    print(dash)
    # 4 . Is letter in word?
    if user_entry in random_word:
            # print(random_word)
            #4.1YES
            #4.1.1 show the letter in my dashed words
            
        index = random_word.find(user_entry)
        
        print(index)
        
        dash.replace(dash[index],user_entry,1) 
          
            #4.1.1 CHECK IF ALL ENRTRIES UNCOVERED.
            #A.IF TRUE GAME OVER
            
        if (dash == random_word):
                print('You Win')
                break
            
            #B. NOT TRUE GO BACK TO ENTER LETTER
            
    else:      
        #4.2 NO
        if life != 0:
                #2. IF LIFE NOT 0 END LOOP GO BACK TO ENTER LETTER
                #1.DECREASE LIFE BY 1.
            life -= 1
        else:
            print('GAME OVER') 
            break   
            #3. ELSE GAMEOVER.

