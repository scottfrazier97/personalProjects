# Sort a list of names by last name instead of first, ignoring capitalization. 

def sort_last_names(names):

    #Grab second item from original names list
    sort_names = sorted(names, key=lambda x: x.split()[-1].lower())

    return sort_names

result = sort_last_names(['Scott Frazier', 'Jared Goff', 'Luka Doncic'])
[print(full_name) for full_name in result]