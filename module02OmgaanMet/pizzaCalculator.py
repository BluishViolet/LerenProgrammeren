small_aantal = int(input("Hoeveel small pizzas wil u?"))
medium_aantal = int(input('Hoeveel medium pizzas?'))
large_aantal = int(input("Hoeveel large pizzas?"))

smallprijs = small_aantal * 4.99
mediumprijs = medium_aantal * 7.99
largeprijs = large_aantal * 9.99

totaal = smallprijs + mediumprijs + largeprijs

print("-------------------------")
print("|Small pizza:  ",    smallprijs,  " euro  |")
print("|Medium pizza: ",    mediumprijs, " euro |")
print("|Large pizza:  ",      largeprijs," euro |")
print("|Totaal:        ",      totaal," euro|")
print("--------------------------")