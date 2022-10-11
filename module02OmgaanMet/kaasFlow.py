start = input("Is de kaas geel?")
if start == "j":
    gatten = input("Zitten er gaten in?")
    if gatten == "j":
        duur = input("Is de kaas belagelijk duur?")
        if duur == "j":
            print("Emmenthaler!")
        else:
            print("Leerdammer")
    else:
        steen = print("Is de kaas hard als steen?")
        if steen == "j":
            print("Parmigiano Reggiano")
        else:
            print("Goudse kaas")
else:
    blauw = input("Heeft de kaas blauwe schimmel?")
    if blauw == "j":
        korst = input("Heeft de kaas een korst?")
        if korst == "j":
            print("Blue de Rochbaron")
        else:
            print("Foume d'Ambert")
    else:
        korst2 = input("Heeft de kaas een korst?")
        if korst2 == "j":
            print("Camebert")
        else:
            print("Mozzarella")