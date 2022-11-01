voorijkostenAfstand = 8
voorijkostenGrootte = 3
voorijkostenDiepte = 1.5
afvoerendGrond = voorijkostenAfstand * voorijkostenGrootte * voorijkostenDiepte
uitgravenpPrijs = 25
uitgravenTotaal = afvoerendGrond * uitgravenpPrijs
vastePrijs = 32.50
prijsPerM3 = afvoerendGrond * vastePrijs
inTotaal = uitgravenTotaal + afvoerendGrond
voorijkostenPerKM = 2.05
afstandBedrijfKM = 60
voorijkostenPerkmTotaal = voorijkostenAfstand * afstandBedrijfKM

print(f'''Offerte voor een zwembad van 8 bij 1,5 meter
Uitgraven:        €{uitgravenTotaal}
Afvoeren grond:   €{afvoerendGrond}
Voorijkosten:     €{voorijkostenPerkmTotaal}
Totaal:           €{inTotaal}  
''')