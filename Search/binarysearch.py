# Use binary search to find a certian item in a list.
# Example: list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
# To find the key: 5


def search(searchList, key):
    list_len = len(searchList)
    mid = int(list_len / 2)
    print ("search middle point is: " + str(searchList[mid]))

    if searchList[mid] == 0 or key < searchList[0] or key > searchList[-1]:
        print ("key not found")
        return key
    list_left = searchList[:mid]
    list_right = searchList[mid:]
    if key == searchList[mid]:
        print ("find it")
        return key
    elif key < searchList[mid]:
        print ("search in list: ", list_left)
        search(list_left, key)
    else:
        print ("search in list: ", list_right)
        search(list_right, key)

if __name__ == "__main__":
    i_list = list(range(1, 55))
    print ("search 77 in list: ", i_list)
    search(i_list, 77)

    i_list = list(range(1, 55))
    print ("search 0 in list: ", i_list)
    search(i_list, 0)

    i_list = list(range(1, 55))
    print ("search 3 in list: ", i_list)
    search(i_list, 3)
