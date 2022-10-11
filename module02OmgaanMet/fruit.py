print('welk fruit zie je?')
langwerpig = input("langwerpig?")
if langwerpig == "j":
    print("**langwerpig!")
    geel = input("geel?")
    if geel == "j":
        print("geel, dus banaan")
        klein = input('kleiner dan 15 cm')
        if klein == "j":
         print("klein, dus bak-banaan")
        #einde geel banaan
    else:
        print("niet geel. dus geen banaan")
        ronde_doorsnee = input("ronde doorsnee?")
        

    #einde langwerpig
else: 
    print("niet langwerpig, dus rond!")
    #einde niet langwerpig