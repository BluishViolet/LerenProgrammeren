print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+    Solicitatieformulier Rumte-vuilnisman      + ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Er wordt een aantal relevante vragen gesteld")
print("Gelieve die naar eer en geweten in te vullen")
print("Als blijkt dat u aan de criteria voldoet dan komt u \naanmerking voor een serieus solicitatiegesprek!")
print(''' "Hier komen de vragen:" 
++++++++++++++++++++++++++++++++++++++++++++++++++++++''')


snorlengte = 0
haarlengte = 0

naam = input("Wat is uw naam?")
geslacht = input("Bent uw een man of vrouw?")
if geslacht == "man":
    snor = input("Heeft uw een snor? J/N" )
    if snor == "j":
        snorlengte = int(input("Breedte van uw snor?"))
elif geslacht == "vrouw":
    haarkleur = input("Wat is uw haar kleur?")
    if haarkleur == "rood":
        haarlengte = int(input("Uw haar lengte?"))
#einde gaslacht vragen

lengteCM = int(input("Wat is uw netto lichaamslengte in hele cm, dus exclusief uw kapsel?"))
gewicht = int(input("Wat is uw lichaamsgweicht in hele kg?"))
diploma = input("Bent uw in bezit van een MBO-Diploma-4 Ondernemer?")
rijbewijs = input("Bent uw in bezit van een Vrachtwagen rijbweijs? J/N ")
hoed = input("Bent uw in bezit van een hoge hoed?")
certif = input ("Bent uw in bezit van een 'Overleven met gevaarlijk personeel?'")

dieren = int(input("Heeft uw ervaring met dieren dressur? Zo ja, hoeveel?"))
jongleren = int(input("Heeft uw ervaring met jongleren? Zo ja, hoeveel?"))
acrobatiek = int(input("Heeft uw ervaring met acrobatiek? Zo ja, hoeveel?"))

if snorlengte >= 10 and diploma == "j" and rijbewijs == "j" and hoed == "j" and certif == "j" or haarlengte > 20 and lengteCM > 150 and gewicht > 90 and dieren > 4 and jongleren > 5 and acrobatiek > 3:
    print(f"Proficiaat {naam}! Uw komt in aanmerking voor een solicitatiegesprek, stuur snel uw CV")
else:
    print(f"{naam}, uw voldoet niet aan ons criteria het spijt ons!")