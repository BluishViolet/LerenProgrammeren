toegangsticket = 7.45 
gameseatpermin = 0.37 / 5
minuten = 45
mensen = 4
toegangsticket_totaal = toegangsticket * mensen
vrTotaal = gameseatpermin * minuten
print("Dit geweldige dagje-uit met" ,mensen, "personen in de Speelhal met", minuten, "minuten VR kost je maar:",round(toegangsticket_totaal + gameseatpermin + vrTotaal,2) , "euro")
