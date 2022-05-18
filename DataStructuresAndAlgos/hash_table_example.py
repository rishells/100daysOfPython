def item_in_common(list1, list2):   # This is an O(N²) solution, not optimal, hence implementing a new one with hash tables below
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


list1 = [1,3,5]
list2 = [2,4,5]

#print(item_in_common(list1,list2))



# solution with Hash Tables O(2n) -> O(n)

def item_in_common_HT(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False

print(item_in_common_HT(list1,list2))

