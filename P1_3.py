class CountingBag(object):
    def __init__(self):
        self._theItems = list()

    def __len__(self):
        return len(self._theItems)

    def __contains__(self, item):
        return item in self._theItems

    def add(self, item):
        self._theItems.append(item)

    def numOf(self, item):
        return self._theItems.count(item)


CB = CountingBag()
for i in range(5):
    CB.add(i)
CB.add(3)
CB.add(4)
CB.add(4)
print(CB._theItems)
print(CB.numOf(2))