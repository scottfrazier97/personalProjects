# You have two lists of tuples representing inventory, Merge and sum quantities by name.

def inventory_merge(inv1, inv2):

    tracker = {}

# 1) Outer loop starts: inv is set to inv1.
# 2) Inner loop runs fully: it iterates over every tuple in inv1, one by one.
# 3) Outer loop moves to next item: inv is now inv2.
# 4) Inner loop runs fully again: it iterates over every tuple in inv2.
# 5) Loop ends when all outer items have been processed.

    for inv in (inv1, inv2):

        for item in inv:

            item_name = str(item[0]).strip().lower()
            item_value = item[1]

            if item_name not in tracker:
                tracker[item_name] = item_value
            else:
                tracker[item_name] += item_value

    sorted_tracker = dict(sorted(tracker.items(), key=lambda item: item[0]))

    #Python returns None along with appropriate data if no return statement is used.
    return sorted_tracker

result = inventory_merge([('apple', 10), ('banana', 5)], [('apple', 3), ('pear', 8)])

for k, v in result.items():
    print(f"{k}: {v}")

