# Given two lists, return the elements that appear in both (no duplicates).

def list_intersection(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    # Converting to sets removes duplicates, as well as allows us to use intersection for common elements
    common_elements = set1.intersection(set2)

    return common_elements

result = list_intersection([1,2,3],[3,4,5])
print(result)