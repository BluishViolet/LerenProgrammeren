voorijkostenAfstand = 8
voorijkostenGrootte = 3
voorijkostenDiepte = 1.5

afvoerendGrond = voorijkostenAfstand * voorijkostenGrootte * voorijkostenDiepte
uitgravenpPrijs = 25
uitgravenTotaal = afvoerendGrond * uitgravenpPrijs
vastePrijs = 32.50
prijsPerM3 = afvoerendGrond * vastePrijs
voorijkostenPerKM = 2.05
afstandBedrijfKM = 60

voorijkostenPerkmTotaal = voorijkostenAfstand * afstandBedrijfKM
betontegel = 20 
betontegelTotaal = betontegel * voorijkostenGrootte
inTotaal = uitgravenTotaal + afvoerendGrond + betontegelTotaal

print(f'''Offerte voor een zwembad van 8 bij 1,5 meter
Uitgraven:        €{uitgravenTotaal}
Afvoeren grond:   €{afvoerendGrond}
Voorijkosten:     €{voorijkostenPerkmTotaal} 
Baton + tegel:    €{betontegelTotaal} 
Totaal:           €{inTotaal}  
''')