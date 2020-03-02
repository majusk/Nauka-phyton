# Napisz program, który liczy za użytkownika. Umożliw użytkownikowi
# wprowadzenie liczby początkowej, liczby końcowej i wielkości odstępu między
# kolejnymi liczbami

start = int(input("Podaj swoja liczbe poczatkowa: "))
finish = int(input("Podaj swoja liczbe koncowa: "))
skip = int(input("Podaj wielkosc odstepu miedzy kolejnymi liczbami: "))

for i in range(start, finish, skip):
    print(i, end=" ")

input("\n\nAby zakonczyc program, nacisnij klawisz Enter.")
