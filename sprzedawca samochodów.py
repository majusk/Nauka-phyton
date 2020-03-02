# program sprzedawca samochodów
# oblicza za jaką kwotę sprzedać samochód

print(
"""

            Program do obliczenia ceny sprzedaży auta

Program umożliwia wpisanie podstawowych danych na temat samochodu, podatków itp. w celu ustalenia
optymalnej ceny sprzedaży.


Poniżej wpisz określone z dokładnością do dwóch miejsc po przecinku.


"""
)

buy_car = float(input("Cena zakupu auta:"))
rejestracja = float(input("Cena rejestracji samochodu:"))
prowizja = buy_car*1.2

sell_car = buy_car + rejestracja + prowizja

print("\n\n Cena sprzedaży auta powinna wynieść:", sell_car)

input("Aby zakończyć program kliknij przycisk Enter")

