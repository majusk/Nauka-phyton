# Program Przegrana bitwa
# Pokazuje działanie pętli nieskończonej

print("Twój samotny bohater jest otoczony przez ogromną armię troli.")
print("Wielka masa ich zgniłozielonych ciał rozciąga się aż po horyzont.")
print("Bohater wyjmuje miesz z pochwy, gotów do stoczenia swojej ostatniej walki.\n")

health = 10
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage
    print("Bogater pokonuje złego trolla, " \
          "Ale odnosi obrażenia i traci", damage, "punkty zdrowia.\n")

print("Twój bohater walczył dzielnie i pokonał", trolls, "trolli.")
print("Lecz niestety Twój bohater już nie żyje.")

print("\n\nAby zakończyć program kliknij Enter.")
