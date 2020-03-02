# Program "Rzut monetą"
# Program wyświetla ile razy wyrzucił reszkę, a ile razy orła na 100 rzutów

import random

numer_rzutu = 0
orzel = 0
reszka = 0

while True:
    numer_rzutu += 1
    moneta = random.randint(1,2)
    if numer_rzutu > 100:
        break
    elif moneta == 1:
        orzel += 1
    else:
        reszka += 1

print("\nStukrotne rzucenie monetą pozwoliło Ci otrzymać następujące wyniki:")
print("Wynik 'orzeł' otrzymano:", orzel, "razy,\na wynik reszka:", reszka, "razy.")

input("\n\naby zakończyć program kliknij enter")
