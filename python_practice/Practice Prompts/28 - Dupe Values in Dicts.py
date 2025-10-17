# Given a list of dictionaries, find all that have duplicate values for a certain key (e.g. `'name'`)

def dupe_dict_vals(dict_name):
    from collections import Counter

    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 25},
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 52},
        {"name": "Scott", "age": 28}
    ]

    temp_lst = []

    for item in data:
        temp_lst.append(item[dict_name])


    ctr = [k for k,v in Counter(temp_lst).items() if v > 1]

    final_output = []
    for key in data:
        if key[dict_name] in ctr:
            final_output.append(key)

    return final_output

result = dupe_dict_vals("name")
print(result)