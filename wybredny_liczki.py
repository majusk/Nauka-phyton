# Program Wybredny licznik
# Program będzie wypisywał liczby od 1 do 10 za pomocą umyślnej pętli nieskończonej

count = 0
while True:
    count += 1
    # zakończ pętlę, jeśli wartość zmiennej count jest większa niż 10
    if count > 10:
        break
    # pomiń liczbę 5
    if count == 5:
        continue
    print(count)

input("\n\nAby zakończyć program, naciśnij przycisk Enter.")
