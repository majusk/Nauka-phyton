# Program Inwentarz bohatera
# Program ten demonstruje zasadę działania list

# utworzę listę zawierającą pewne elementy i wyświetl jej zawartość za
# pomocą pętli for
inventory = ["miecz", "zbroja","tarcza","napój uzdrawiający"]
print("Elementy Twojego inwentarza:")
for item in inventory:
    print(item)

#wyświetlam długość listy inventory
print("Twój dobytek zawiera", len(inventory), "elementy(-ów).")

input("\nAby kontynuowac gre, nacisnij klawisz enter.")

# sprawdź, czy element należy do listy, za pomocą operatora in
if "napój uzdrawiający" in inventory:
    print("\nDożyjesz dnia, w którym stoczysz walkę.")

# wyświetlam jeden element listy wskazany przez indeks
index = int(input("\nWprowadź indeks elementu inwentarza: "))
print("Pod indeksem", index, "znajduje się", inventory[index])

# wyświetlam wycinek listy
start = int(input("\nWprowadź indeks wyznaczający początek wycinka listy: "))
finish = int(input("\nWprowadź indeks wyznaczający koniec wycinka listy: "))
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

# dokonuję konketanacji dwóch list
chest = ["złoto", "klejnoty"]
print("Znajdujesz skrzynię, która zawiera:", end=" ")
print(chest)
print("Dodajesz zawartość skrzyni do swojego inwentarza.")
inventory += chest
print("Twój aktualny inwentarz to:")
print(inventory)

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

# przypisuję nową zawartość do listy poprzez indeks
print("Wymieniasz swój miecz na kuszę.")
inventory[0] = "kusza"
print("Twój aktualny inwentarz to:")
print(inventory)

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

# przypisuję nowy wycinek do lsty
print("Zużywasz swoje złoto i klejnoty na zakup kuli do wróżenia.")
inventory[4:6] = ["kula do wróżenia"]
print("Twój aktualny inwentarz to: ")
print(inventory)

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

# usuwam element z listy
print("W wielkiej bitwie zostaje zniszczona Twoja tarcza")
del inventory[2]
print("Twój aktualny inventarz to: ")
print(inventory)

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

# usuwam wycinek z aktualnej listy
print("Twoja kusza i zbroja zostały skradzione przez złodziei")
del inventory[:2]
print("Twój aktualny inwentarz to: ")
print(inventory)

input("\nAby zakończyć grę, naciśnij klawisz Enter.")


