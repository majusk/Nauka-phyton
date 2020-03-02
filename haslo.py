# hasło
# demonstruje instrukcję if

print("Witaj w systemie firmy Bezpieczny komputer SA")
print("-- bezpieczeństwo to podstawa naszego działania\n")

password= input("Wprowadź hasło: ")

if password == "sekret":
    print("Dostęp został udzielony")
    print("Musisz być kimś naprawdę ważnym")

if password != "sekret":
    print("Dostęp nie został udzielony")
    

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
