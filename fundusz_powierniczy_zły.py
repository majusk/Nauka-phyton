# uczestnik funduszu powierniczego - niepoprawna wersja
# demonstruje błąd logiczny

print(
"""
            Uczestnik funduszu powierniczego

Sumuje Twoje miesięcze wydatki, żeby Twój fundusz powierniczy się nie wyczerpał
(bo wtedy byłbyś zmuszony do podjęcia prawdziwej pracy).

Wprowadź swoje wymagane miesięczne koszty. Ponieważ jesteś bogaty, zignoruj
groszei swoje kwoty podaj w pełnych złotych.

"""
)

car = input("Serwis mercedesa:")
rent = input("Apartament w Śródmieściu:")
jet = input("Wynajem prywatnego samolotu:")
gifts = input("Podarunki:")
food = input("Obiady w restauracjach:")
staff = input("Personel (służba domowa, kucharz, kierowca, asystent):")
guru = input("Osobisty guru i coach:")
games = input("Gry komputerowe:")

total = car + rent + jet + gifts + food + staff + guru + games

print("\nOgółem:", total)

input("\n\nAby zakończyć program kliknij Enter.")
