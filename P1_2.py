class GrabBag(object):
    def __init__(self):
        self._theItems = list()
        # print(self._theItems)

    def __len__(self):
        return len(self._theItems)

    def __contains__(self, item):
        return item in self._theItems

    def add(self, item):
        self._theItems.append(item)

    def grabItem(self, grabNo):
        del self._theItems[grabNo]
        return self._theItems


#     def __iter__(self):
#         return _GrabBagIterator(self._theItems)
#
# class _GrabBagIterator():
#     def __init__(self, theList):
#         self._grabBagItems = theList
#         self._curItem = 0


gB = GrabBag()
# print(type(gB))

for i in range(5):
    gB.add(i)

print(gB._theItems)

print(gB.__contains__(2))
print(gB.grabItem(2))

