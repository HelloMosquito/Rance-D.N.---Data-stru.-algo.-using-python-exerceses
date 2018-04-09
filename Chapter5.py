def binarySearch(item, sortedlist):

    if len(sortedlist) == 0 or (len(sortedlist) == 1 and item != sortedlist[0]):
        print("there is no such a No. of ", item)
        return item
        # return False

    n = len(sortedlist)
    middle_po = int(n / 2)
    print(middle_po)
    target = sortedlist[middle_po]
    print(target)
    if item == target:
        print("target is ", target)
        return item
        # return True
    elif item < target:
        nextList = sortedlist[0:middle_po]
        print(nextList)
        binarySearch(item, nextList)

    else:
        nextList = sortedlist[middle_po:]
        print(nextList)
        binarySearch(item, nextList)


l = list(range(1,11))
print(l)
a = 0
x = binarySearch(a, l)
print(x)
# it will print None because of the recursion. When the last run of the func, it will return True/False to its previous
# layer func. Thus, the previous one will receive a bool value but will not return anything to one more upper layer func.
# At last, when it reach the first layer function, it won't return anythin, therefore, the print(x) in main will print None.








