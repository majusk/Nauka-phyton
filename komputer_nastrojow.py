# Komputer nastrojów
# Demonstruje klauzulę elif w instrukcji if

import random

print("Wyczuwam Twoją energię użytkowniku. Twoje prawdziwe emocje znajdują odbiie na moim ekranie.")
print("Jesteś...")

mood = random.randint(1,3)

if mood == 1:
    # szczęśliwy
    print(
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       -----------
                   """)

elif mood == 2:
    # obojętny
    print(
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | ------  |
       |         |
       -----------
                   """)

elif mood == 3:
    # smutny
    print(
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       |  .'.    |
       | '   '   |
       -----------
                   """)

else:
    print("Nieprawidłowa wartość nastroju! (musisz być naprawdę w złym humorze.")

print("...dzisiaj.")

input("\n\nAby zakończyć program kliknj Enter.")
