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
    def __init__(self,row, col):
        self._theGrid = Array2D(row, col)
        self._theGrid.clear(0)
            

    def scaleBy(self, scalar):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self._theGrid[i][j] *=scalar

    def transpose(self):
        transMatrix = Matrix(self.numCols(),self.numRows())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                transMatrix._theGrid[j][i] = self._theGrid[i][j]

        return transMatrix

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), "sizes of matrix are not matched"
        addMatrix = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                addMatrix[i][j] = self._theGrid[i][j] + rhsMatrix[i][j]
        return addMatrix
    def subtract(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), "sizes of matrix are not matched"
        addMatrix = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                addMatrix[i][j] = self._theGrid[i][j] - rhsMatrix[i][j]
        return addMatrix



class LifeGrid(object):
    
    live = 1
    dead = 0
    
    def __init__(self, row, col):
        self._lifegrid = Array2D(row, col)
        self._lifegrid.clear(dead)
        
    def numRows(self):
        return self._lifegrid.numRows()
    def numCols(self):
        return self._lifegrid.numCols()
    
    # def configure(self, coordList):
    #     assert len(coordList) == 2, "this is a 2D life grid, you should input as (indexR, indexC)"
    #     indexR = coordList[0]
    #     indexC = coordList[1]
    #     assert indexR >=0 and indexR < self.numRows() and indexC >=0 and indexC < self.numCols(), "index out of range"
    #     self._lifegrid[indexR][indexC] = LifeGrid.live
        
    def clearCell(self, row, col):
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "index out of range"
        self._lifegrid[row][col] = LifeGrid.dead
        
    def setCell(self, row, col):
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "index out of range"
        self._lifegrid[row][col] = LifeGrid.live
        
    def isLiveCell(self, row, col):
        return self._lifegrid[row][col] == LifeGrid.live
        # assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "index out of range"
        # if self._lifegrid[row][col] == LifeGrid.live
        #     return True
        # elif self._lifegrid[row][col] == LifeGrid.dead
        #     return False
    
    def numLiveNeighbors(self, row, col):
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "index out of range"
        numLive = 0
        indexNeighbors = self.Neighbors(row, col)
        for item in indexNeighbors:
            if item[0] >= 0 and item[0] < self.numRows() and item[1] >= 0 and item[1] < self.numCols() and \
                    self.isLiveCell(item[0], item[1]):
                numLive += 1
                
        return numLive
                
                                 
    def Neighbors(self, row, col):
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "index out of range"
        NeighborsList = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), \
                         (row+1, col), (row+1, col+1)]
        return NeighborsList
        
















