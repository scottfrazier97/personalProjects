def speed(user):
    while True:
        print("- " * 5)

        mphTOKPHconversion = round(user / 1.609, 2)
        spacestationspeedKPH = 10650
        difference = mphTOKPHconversion - spacestationspeedKPH
        smalldiff = spacestationspeedKPH - mphTOKPHconversion

        print(f"{mphTOKPHconversion} KPH")
        print("- " * 5)

        if mphTOKPHconversion == spacestationspeedKPH:
            print(f"In case you were wondering, the resulting speed in KPH you received is equal to the speed of the \nInternational Space Station, which is {spacestationspeedKPH} KPH.")
        elif mphTOKPHconversion > spacestationspeedKPH: 
            print(f"In case you were wondering, the resulting speed in KPH you received is {difference} KPH faster than that of the \nInternational Space Station in KPH, which is {spacestationspeedKPH} KPH.")
        elif mphTOKPHconversion < spacestationspeedKPH: 
            print(f"In case you were wondering, the resulting speed in KPH you received is {smalldiff} KPH slower than that of the \nInternational Space Station in KPH, which is {spacestationspeedKPH} KPH.")

        print("- " * 15)
        print("Thanks for using the speed converter", "Be sure to come again.", sep=' - ')
        break

user = float(input("Welcome! To begin, enter a speed in MPH: "))
speed(user)
