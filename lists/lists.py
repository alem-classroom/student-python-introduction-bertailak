def size_of_list(list):
    # return size of list
    return len(list)

def add_elem_to_list(list, elem):
    # add elem to list and return the list
    list.append(elem)
    return list

def delete_elem_from_list(list, index = -1):
    # delete element from list, such that its index is index
    # if index is invalid, return empty list
    if(-len(list)<=index<len(list)):
        return list.pop(index)
    else:
        return []
    

def count_elements_in_list(list, x):
    # count elements in the list that are equal to x and return the count
    return list.count(x)

def sort_list(list):
    # return sorted list
    return list.sort()

def reverse(list):
    # return reversed list
    return list.reverse()

#print(delete_elem_from_list([1, 2, 3], 1))
#print(count_elements_in_list([1, 2, 3, 1], 1))

#print(size_of_list([1, 2, 3, 1]))
