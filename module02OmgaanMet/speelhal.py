toegangsticket = 7.45 
minuten = int(input('Hoe lang zal de VR-Gameseat duren?'))
mensen = int(input('Aantal mensen:'))
gameseatpermin = 0.37 * minuten

toegangsticket_totaal = toegangsticket * mensen
vrTotaal = gameseatpermin * minuten

print("Dit geweldige dagje-uit met" ,mensen, "personen in de Speelhal met", minuten, "minuten VR kost je maar:",round(toegangsticket_totaal + gameseatpermin + vrTotaal,2) , "euro")
