# Program "Jaka to liczba?"
# Komputer wybiera losowo liczbę z zakresu 1 do 100
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy podana liczba jest za duża czy za mała lub prawidłowa

# Zawsze na początku pobieram wykorzystywany w programie moduł
import random
import sys

print("\tWitaj w grze 'Jaka to liczba'!")
print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.")

# Ustaw wartości początkowe- wylosuj liczbę przed odgadywaniem przez użytkownika
the_number = random.randint(1,100)
guess = int(input("Ta liczba to: "))
tries = 1

# Pętla zgadywania
while guess != the_number:
    if tries > 3:
        print("Szkoda. Próbowałeś zbyt wiele razy")
        print("Ta liczba to", the_number)
        sys.exit()
        
    elif guess > the_number:
        print("Za duża...")
    elif guess < the_number:
        print("Za mała...")
        
    guess = int(input("Ta liczba to:"))
    tries += 1

    
    
    
   
# Jeżeli użytkownik odgadnie liczbę, to warunek pętli "while guess != the_nuber
# otrzymuje wartość false i pętla się kończy
print("Odgadłeś! Ta liczba to", the_number)
print("Do osiągnięcia sukcesu potrzebowałe tylko", tries, "prób!\n")


input("\n\nAby zakończyć program kliknij klawisz Enter.")
