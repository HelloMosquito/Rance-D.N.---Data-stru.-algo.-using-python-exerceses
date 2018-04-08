class ArrayADT(object):
    def __init__(self, size):
        self.size = size
        self.array = [None] * self.size


    def __len__(self):
        return len(self.array)

    def getitem(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.index = index
        self.value = value
        self.array[index] = value

    def clearing(self, value):
        self.array = [value] * self.size







arr = ArrayADT(5)
for i in range(5):
    arr.__setitem__(i, i*2)
arr.clearing(5)

print(arr.array)
print(len(arr.array))


