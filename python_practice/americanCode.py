freedom = "AMERICA!"
is_free_country = True
while is_free_country:
    print('America is FREE, That is what I am talking about!', freedom)
    break

bestCountryEver = [liberty for liberty in freedom]
print(bestCountryEver)

for freedom in freedom:
    print(freedom)

for i in range(4):
    print('*************-----------------')
for x in range(4):
    print('------------------------------')

yearLiberated = int(1776)
currentYear = int(input("Enter the current year: "))
def yearsSince():
    yearsSince = currentYear - yearLiberated
    print(f"It has been {yearsSince} years since America gained it's independence from Great Britain!")

    if yearsSince == 300:
        print("It has been 300 years since America has gained it's independence.")
    elif yearsSince > 300:
        print("It has been more than 300 years since America has gained it's indepence from Great Britain.")
    elif currentYear < 1776:
        print("Something must have been lost in the shadow realm. QUICK MARTY, WE HAVE TO GO BACK TO THE FUTURE!")
    else:
        pass
yearsSince()