aantal_croissantjes = int(input('Hoeveel croissantjes gaat u kopen?'))
prijs_croissantjes = 0.39
aantal_stokbroden = int(input('Hoeveel stokbroden?'))
prijs_stokbroden = 2.78
kortingsbonnen = 2
aantal_kortingsbonnen = int(input('Aantal kortingsbonnen:'))


croissantjes_in_totaal = aantal_croissantjes * prijs_croissantjes
stokbroden_in_totaal = aantal_stokbroden * prijs_stokbroden

totaal = croissantjes_in_totaal + stokbroden_in_totaal


print("De feestlunch kost je bij de bakker", round(totaal/kortingsbonnen * aantal_kortingsbonnen ,2), "euro voor de" ,aantal_croissantjes, "croissantjes en de", aantal_stokbroden, "stokbroden als de", aantal_kortingsbonnen, "kortingsbonnen nog geldig zijn!")