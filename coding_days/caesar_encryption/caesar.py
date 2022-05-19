# 29-40 BIT ENCRYPTION
#DAY 8 PROJECT ENCRYPTION. AND DECRYPTION.
# AUTHOR LAWRENCE
# VERSION NO: 001
# LICENCE FREE TO USE.
#MADE IT A LITTLE BIT FUN SECOND PROJECT WITH PYTHON.

#FLOW CHART
    # 1. GET USER TO ENTER THE TEXT HE/SHE WANTS TO ENCRYPT
    # 2. ASK FOR THE SECRET WORD 
    # 3. ENCRPT THE WORD PRESENTING IT TO THE USER 
    # 4. FOR DECRPTION DO THE OPPOSITE. 

import time

v2_banner = """
     DEARLY BELOVED WELCOME TO 100BC-44BC ANCIENT ROME MESSAGE CENTER  @@                          
                                                               @&%#%###%%#%@@@.                     
                                                            @%#%%%%%%%%%%%((%%&@@                   
 @#  1. SEND ENCODED MESSAGE TO FELLOW ROMAN   ,...,..,..,,#(#%%%%%%#%%%%%#/(#(##/,.,.,,.,.... ,.,# 
 @   2. DECODE MESSAGE RECIEVED                .,...,..,,,/(##%&%&%%%%%%%##*##*/###.,,,,........... 
 @   3. CAESARS ARENA CHARGED ENCRYPTION         ,.....,.//#****/#****#%%/%/#/###/(,,,....,........ 
     4. CAESARS ARENA CHARGED DECRYPTION.       .......*,/*%#*/%%%(/(((*(%//*/#/**.,....,,....... 
     5. Exit                                    ....,,,/#%%%##%#%%%##%&##%#/.#./,........,...... 
             . .    ..... ..............,........,......,.((#%#,*/(//#%####((,,,*(#...,...,.,....,. 
                    .   .   ..... .,..,.....,..,....,....,,/#((#*,#%(#/#((/((/#/(.,.......... ..... 
 @                @* .    .  .   ..,. ,........,..,,..,..../(/#*////%#(#(((//,,,,.........,..,..... 
 &       @@ @# @@ @*.@ @@ #@ *@@&.....,,.......,.,,,.....,..*/#####%%##(*(**,/,,...., ........,, .. 
 &       @@ @# @@ @*.@ @@ #@ *@@@ ...........,.,...,..,.,,...,/,,,***,,**,((*,........,.. ,........ 
 &     %@/  .&&&@ @*,@  &&/@ .&@*.........,.....,..,,,,,,..,*(**,,**,,**/((#,....,.,,....,,........@
 &.                          .    ........ ,*.......,,,...,.###(***/%%(/(##%,....,.,......... ,....@
 &..  &@  #@  %&.   &%   %&   *&#.,..&....((####*......#(,#%#(###(/*(((######*(*.........,.,..,....@
 &....@@     ,@@@#@@@@@.@@@&,.@@@@*@(/*(#%##*.*//(*,#%#%%%%(##(##%(((#%#/(###%*#(//(....,..,.,,...,@
 &.....%@@@ .@@@@% &@@@.#@@@,*@@&@*@(*(#%((#%%%((/,.#,***/,(%%%###%%#%#%%##%%%%(((,%((#/.....,. ... 
 &...... ..,,,,,,,********,**,,,/,*(((/#%%#%#%%#%%%%%%((#*#*((%%###(#%%%%%%%%%#(##%%/*/*  ......,,, 
"""   
image = """                                                                   @@                          
                                                               @&%#%###%%#%@@@.                     
                                                            @%#%%%%%%%%%%%((%%&@@                   
 @#. .... ..........,..,..,....................,...,..,..,,#(#%%%%%%#%%%%%#/(#(##/,.,.,,.,.... ,.,# 
 @           .   .. .... ....... ...,.......,...,...,..,,,/(##%&%&%%%%%%%##*##*/###.,,,,........... 
 @              .   .  .   ............,...............,.//#****/#****#%%/%/#/###/(,,,....,........ 
    AUTHOR LAWRENCE  .   ........  .....,. ,....,,........*,/*%#*/%%%(/(((*(%//*/#/**.,....,,....... 
    V:001          .  ...............,...,. ...........,,,/#%%%##%#%%%##%&##%#/.#./,........,...... 
             . .    ..... ..............,........,......,.((#%#,*/(//#%####((,,,*(#...,...,.,....,. 
                    .   .   ..... .,..,.....,..,....,....,,/#((#*,#%(#/#((/((/#/(.,.......... ..... 
 @                @* .    .  .   ..,. ,........,..,,..,..../(/#*////%#(#(((//,,,,.........,..,..... 
 &       @@ @# @@ @*.@ @@ #@ *@@&.....,,.......,.,,,.....,..*/#####%%##(*(**,/,,...., ........,, .. 
 &       @@ @# @@ @*.@ @@ #@ *@@@ ...........,.,...,..,.,,...,/,,,***,,**,((*,........,.. ,........ 
 &     %@/  .&&&@ @*,@  &&/@ .&@*.........,.....,..,,,,,,..,*(**,,**,,**/((#,....,.,,....,,........@
 &.                          .    ........ ,*.......,,,...,.###(***/%%(/(##%,....,.,......... ,....@
 &..  &@  #@  %&.   &%   %&   *&#.,..&....((####*......#(,#%#(###(/*(((######*(*.........,.,..,....@
 &....@@     ,@@@#@@@@@.@@@&,.@@@@*@(/*(#%##*.*//(*,#%#%%%%(##(##%(((#%#/(###%*#(//(....,..,.,,...,@
 &.....%@@@ .@@@@% &@@@.#@@@,*@@&@*@(*(#%((#%%%((/,.#,***/,(%%%###%%#%#%%##%%%%(((,%((#/.....,. ... 
 &...... ..,,,,,,,********,**,,,/,*(((/#%%#%#%%#%%%%%%((#*#*((%%###(#%%%%%%%%%#(##%%/*/*  ......,,, 
"""                 


position_shift = ['a','b','c','d','e','f','g','h','i',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                  'j','k','l','m','n','o','p','S','q','r',
                  'K', 'L', 'M','Z' ,'N', 'O', 'P', 'Q', 'R',  
                  's','t','u','v','w','x','y','z',' ','.','?',
                  'T','U' ,'V','W' ,'X', 'Y',  'I']

position_shift_arena = [
                  'a','b','c','d','e','f','g','h','i',
                  'A','B','C','D','E','F','G','H','r',
                  'j','k','l','1','m','n','o','p','S','q',
                  'K', 'L', 'M','Z' ,'N', 'O', 'P', 'Q', 'R',  
                  's','t','6','u','v','w','9','x','y','z',' ','.','?',
                  'T','U' ,'V','W' ,'X', 'Y', 'I','7',
                  '4','2','5','3']



def encrypt(word="I came I saw I conquered",secret_key=13,search=position_shift):
    word = str(input("Enter Message: "))
    secret_key = int(input("Enter Secret Key: "))
    output = ''
    
    if secret_key > len(search):
        secret_key=  secret_key % len(search) 
        # print(secret_key)
        
    for i in word:
        #FOR CASES WHERE THE SECRET KEY IS GREATER THAN AVAILABLE KEYWORDS
        #COUNT THE NUMBER OF TIMES WE HAVE LOOPED OVER VALUES IN THE LIST
        #THAT IS EQUAL TO GETTING THE REMAINDER WHICH WILL BE OUR SECRET KEY.
        
        index_po = search.index(i) + secret_key
        if index_po >= len(search):
            index_po = index_po % len(search)
            output += search[index_po]
            # print("inside if ",index_po)
        else:
            # print(index_po)
            output += search[index_po]
        
    print(f"\t Message: {output}")
    time.sleep(10)

def decrypt(word="I came I saw I conquered",secret_key=13,search=position_shift):
    word = str(input("Enter Message: "))
    secret_key = int(input("Enter Secret Key: "))
    output = ''
    
    if secret_key > len(search):
        secret_key=  secret_key % len(search) 
        print(secret_key)
        
    for i in word:
        #FOR CASES WHERE THE SECRET KEY IS GREATER THAN AVAILABLE KEYWORDS
        #COUNT THE NUMBER OF TIMES WE HAVE LOOPED OVER VALUES IN THE LIST
        #THAT IS EQUAL TO GETTING THE REMAINDER WHICH WILL BE OUR SECRET KEY.
        
        index_po = search.index(i) - secret_key
        if index_po >= len(search):
            index_po = index_po % len(search)
            output += search[index_po]
            # print("inside if ",index_po)
        else:
            print(index_po)
            output += search[index_po]
        
    print(f"\t Decoded Message Is : {output}")
    time.sleep(8)
    
def user_choice(choice=1):
    banner= """
    DEARLY BELOVED WELCOME TO 100BC-44BC ANCIENT ROME MESSAGE CENTER\n
     1. SEND ENCODED MESSAGE TO FELLOW ROMAN\n
     2. DECODE MESSAGE RECIEVED\n
     3. CAESARS ARENA CHARGED ENCRYPTION\n
     4. CAESARS ARENA CHARGED DECRYPTION\n
     5. CREDITS PICTURE(AUTHOR)
    """
    banner
    while 1:
        print(banner)
        
        try:
            choice = int(input("\tENTER CHOICE 1-5 : "))
  
            if choice == 1:
                encrypt()
            elif choice == 2:
                decrypt()
            elif choice == 3:
                encrypt(search=position_shift_arena)
            elif choice == 4 :
                decrypt(search=position_shift_arena)
            elif choice == 5 :
                print(image)
                time.sleep(10)
                break
            else:
                pass
        except:
            print("\n\t  SOLDIERS CEASE HIM!")
           
if  __name__ =="__main__":
    # "PRINT THE WELCOME SCREEN"
    user_choice()
