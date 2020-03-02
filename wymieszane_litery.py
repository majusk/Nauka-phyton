# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinien odgadnąć pierwsze słowo

import random

# utwórz sekwencję słów do wyboru
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")

# wybierz losowo jedno słowo z krotki WORDS

word = random.choice(WORDS)

# utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna

correct = word

# utwórz 'pomieszaną' wersję słowa
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

# rozpocznij grę

print(
"""

          Witaj w grze 'Wymieszane litery'!

    Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij Enter bez podawania odpowiedzi.)
"""
)
print("Zgadnij, jakie to słowo:", jumble)

guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess !=" ":
    print("Niestety, to nie to słowo.")
    guess = input("Twoja odpowiedź: ")

if guess == correct:
    print("Zgadza się! Zgadłeś!\n")

print("Dziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
