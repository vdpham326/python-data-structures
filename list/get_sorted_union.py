
list1 = [1, 3, 5, 7, 9]
list2 = [1, 2, 3, 6, 8, 9, 10]

def get_sorted_union(list1, list2):
    i = 0
    j = 0
    new_list = []
    while i < len(list1) and j < len(list1):
        if list1[i] not in list2:
            new_list.append(list1[i])
            i += 1
        elif list2[j] not in list1:
            new_list.append(list2[j])
            j += 1
    return new_list

print(get_sorted_union(list1, list2))