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

buy_car = float(input("Cena zakupu auta (zł netto):"))
rejestracja = float(input("Cena rejestracji samochodu(zł netto):"))
prowizja = buy_car*float(input("Prowizja narzucona przez dealera (wpisz procent po kropce np. 0.20):"))

sell_car = (buy_car + rejestracja + prowizja)*1.23 #suma w nawiasie to cena netto przemnożona przez opodatkowanie 23% (1.23)

print("\n\n Cena sprzedaży auta powinna wynieść:", sell_car ,"zł brutto.")

input("Aby zakończyć program kliknij przycisk Enter")

