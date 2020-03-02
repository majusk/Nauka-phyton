# Inwentarz bohatera
# Demonstruje tworzenie krotek

# utwórz pustą krotkę

# utwórz krotkę zawierającą pewne elementy
inventory = ("miecz",
             "zbroja",
             "tarcza",
             "napój uzdrawiający")

# wyświetl każdy element krotki
print("\nElementy Twojego wyposażenia:")
for item in inventory:
    print(item)

input("\n\nAby kontynuować grę kliknij Enter.")

# wyświetl długość krotki
print("Twój dobytek zawiera", len(inventory), "elementy(-ów).")

input("\Aby kontynuowac gre, nacisnij klawisz Enter.")

# sprawdź, czy dany element należy do krotki za pomocąą operatora in
if "napój uzdrawiający" in inventory:
    print("Dożyjesz dnia, w którym stoczysz walkę.")

# wyświetl jeden element wskazany przez indeks
index= int(input("\nWprowadź indeks elementu inwentarza: "))
print("Pod indeksem", index, "znajduje się", inventory[index])

# wyświetl wycinek elementów z krotki
start = int(input("\nWprowadź indeks wyznaczający początek wycinka krotki: "))
finish = int(input("\nWprowadź indeks wyznaczający koniec wycinka krotki: "))
print("inventory[", start, ":", finish, "] tp", end=" ")
print(inventory[start:finish])

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

# dokonaj konkatenacji dwóch krotek

chest = ("złoto", "klejnoty")
print("Znajdujesz skrzynię, która zawiera:")
print(chest)
print("Dodajesz zawartośc skrzyni do swojego inwentarza.")
inventory += chest
print("Twó aktualny inwentarz zawiera:")
print(inventory)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
