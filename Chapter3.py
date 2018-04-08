# class Set():
#     def __init__(self):
#         self._set = list()
#
#         # self.clear()
#
#     def __len__(self):
#         return len(self._set)
#
#     def __contains__(self, item):
#         return item in self._set
#
#     def add(self, element):
#         if element not in self._set:
#             self._set.append(element)
#
#     def remove(self, element):
#         assert element in self._set, "this element is not in this set"
#         self._set.remove(element)
#
#     def __eq__(self, setB):
#         if len(self._set) != len(setB):
#             return False
#         else:
#             return self.isSubSetOf(setB)
#
#     def isSubSetOf(self, setB):
#         for item in self._set:
#             if item not in setB:
#                 return False
#         return True
#
#     def union(self, setB):
#         newSet = setB
#         for item in self._set:
#             if item not in newSet:
#                 newSet.append(item)
#         return newSet

class _MapEntry(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class _MapIterator(object):
    def __init__(self, theMap):
        self._mapRef = theMap
        self._curNdx = 0

    def __iter__(self):
        return self


    def __next__(self):
        if self._curNdx < len(self._mapRef):
            value = self._mapRef[self._curNdx]
            self._curNdx += 1
            return value
        else:
            raise StopIteration


class Map(object):
    def __init__(self):
        self._entryList = list()

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, key):
        return key in self._entryList

    def add(self, key, value):
        indexKey = self._findIndexKey(key)
        if indexKey is not None:
            self._entryList[indexKey].key = value
            return False
        else:
            self._entryList.append(_MapEntry(key, value))
            return True

    def valueOf(self, key):
        indexKey = self._findIndexKey(key)
        assert indexKey is not None, "invalid map key"
        return self._entryList[indexKey].value


    def remove(self, key):
        indexKey = self._findIndexKey(key)
        assert indexKey is not None, "invalid map key"
        self._entryList.remove(indexKey)

    def __iter__(self):
        return _MapIterator(self._entryList)


    def _findIndexKey(self, key):
        size = len(self._entryList)
        for i in range(size):
            if self._entryList[i].key == key:
                return i
        return None

# ===== TEST ======================================

m = Map()
m.add('aaa', 1)
m.add(2, 'bbb')
m.add('c', 'd')
m.add(5, 111)
print(m.valueOf(5))


# =================================================
