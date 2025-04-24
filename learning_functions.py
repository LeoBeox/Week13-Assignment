mylist = [1, 2, 3, 4, 5, 100, 75, 1090, 9999]

def findMaxInList(list):
    x = list[0]
    for number in list:
        y = number
        if y >= x:
            largest = y
        x = y
    
    return largest


print(findMaxInList(mylist))