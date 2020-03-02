# Program Ciastko z Wróżbą
# Losuje pięć losowych wróżb

import random

cookie_text = random.randint(1,3)

if cookie_text == 1:
    print("lodówką zębów nie umyjesz")

elif cookie_text == 2:
    print("raz świeci słońce raz pada deszcz")

elif cookie_text == 3:
    print("hej ho do pracy by się szło")

else:
    print("nie ma takiego ciasteczka z wróżbą!")

input("Aby zakończyć program kliknij Enter")

    
