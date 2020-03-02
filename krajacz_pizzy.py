# Program "Kraacz pizzy
# Demonstruje tworzenie wycinków łańcucha z już istniejącego


word = "pizza"

print("Wprowadź początkowy i końowy indeks wycinka łańcucha 'pizza'.")
print("Aby zakończyć tworzenie wycinków, w odpowiedzi na monit 'Początek:'\n"
      + "naciśnij klawisz Enter.")

start = None
while start != "":
    start = (input("\nPoczątek:"))

    if start:
        start = int(start)

        finish = int(input("Koniec:"))

        print("word[", start, ":", finish, "] to", end=" ")
        print(word[start:finish])

hinput("\n\nAby zakończyć program, naciśnij klawisz Enter.")
