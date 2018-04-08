import ctypes
class Array(object):

    def __init__(self, size):
        assert size > 0, "should > 0"
        self.size = size
        PyArrayType = ctypes.py_object*size
        self._elements = PyArrayType()
        self.clear(None)


    def __len__(self):
        return self.size

    def __getitem__(self, index):
        assert index >= 0 and index <self.size, "Array subscript out of range"
        return self._elements[index]

        # return self.array[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < self.size, "Array subscript out of range"
        self._elements[index] = value

        # self.index = index
        # self.value = value
        # self.array[index] = value

    def clear(self, value):
        for i in range(self.size):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator(object):

    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


# ========== TEST =========================
# arr = ArrayADT(5)
#
# for i in range(5):
#     arr.__setitem__(i,i*2)


# arr = ArrayADT(-5)
# for i in range(5):
#     arr.__setitem__(i, i*2)
# arr.clearing(5)
#
# print(arr.array)
# print(len(arr.array))
# =========================================


class Array2D(object):
    def __init__(self, row, col):

        self._theRows = Array(row)
        for i in range(row):
            self._theRows[i] = Array(col)


        # assert row >= 0 and col >= 0, "row and col index must >= 0"
        # self.row = row
        # self.col = col
        # self.pyArray2DRow = ctypes.py_object*row
        # self.clear(value)
        # self.pyArray2DCol = self.pyArray2DRow * col


    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def clear(self, value):
        for r in range(self.numRows()):
            self._theRows[r].clear(value)

        # for eachCol in self._theRows:
        #     eachCol.clear(value)



    def __getitem__(self, indexTuple):  #__getitem__only have one parameter, so a tuple has to be used as the index of the 2D array
        assert len(indexTuple) == 2, "this is a 2D array, you have to put the index as (x,y)"
        indexRow = indexTuple[0]
        indexCol = indexTuple[1]
        assert indexRow >= 0 and indexRow < self.numRows() and indexCol >= 0 and indexCol < self.numCols(), "index out of range"
        return self._theRows[indexRow][indexCol]

    def __setitem__(self, indexTuple, value):
        assert len(indexTuple) == 2, "this is a 2D array, you have to put the index as (x,y)"
        indexRow = indexTuple[0]
        indexCol = indexTuple[1]
        assert indexRow >= 0 and indexRow < self.numRows() and indexCol >= 0 and indexCol < self.numCols(), "index out of range"
        self._theRows[indexRow][indexCol] = value



# ========== TEST =========================
# TowDArray = Array2D(3,4)
# print("====>")
# print(TowDArray)
# TowDArray.clear(5)
# print("Rows No. is", TowDArray.numRows())
# print("Cols No. is", TowDArray.numCols())
# print(TowDArray._theRows)
#
# for i in range(3):
#     # print("row is", i)
#     for j in range(4):
#         print(TowDArray[(i,j)], end="")
#
#     print("")
# =========================================

class Matrix(Array2D):
    # def __init__(self,row, col):
    #     pass

    def scaleBy(self, scalar):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self._theRows[i][j] *=scalar

    def transpose(self):
        transMatrix = Matrix(self.numCols(),self.numRows())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                transMatrix._theRows[j][i] = self._theRows[i][j]

        return transMatrix

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), "sizes of matrix are not matched"
        addMatrix = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                addMatrix[i][j] = self._theRows[i][j] + rhsMatrix[i][j]
        return addMatrix


















