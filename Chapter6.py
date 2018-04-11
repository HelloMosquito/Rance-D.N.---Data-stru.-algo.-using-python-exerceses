# class BagListNode(object):
#     def __init__(self):
#         self.data = None
#         self.next = None
#
#     class Bag(object):
#     def __init__(self):
#         self._head = None
#         self._size = 0
#         # self.data = None
#         # self.next = None
#
#     # class BagLinkList(object):
#     # def __init__(self):
#     # 	self.head = None
#     # 	self.item = Bag()
#
#     def __len__(self):
#         return self._size
#         # curNode = head
#         # size = 0
#         # while curNode is not None:
#         # 	curNode = curNode.next
#         # 	size += 1
#         # return size
#
#     def __contains__(self, item):
#         curNode = self.head
#         while curNode is not None and item != curNode.data:
#             curNode = curNode.next
#         return curNode is not None
#         # return item == curNode.data
#
#     def add(self, item):
#         newNode = BagListNode(item)
#         newNode.next = self._head
#         self._head = newNode
#         self._size += 1
#
#     def remove(self, item):
#         curNode = self._head
#         while curNode is not None and item != curNode.data:
#             preNode = curNode
#             curNode = curNode.next
#
#         if curNode is not None:
#             self._size -= 1
#             if curNode is head:
#                 self._head = self._head.next
#             else:
#                 preNode.next = curNode.next
#             return curNode.data
#         else:
#             # raise "no such an item"
#             raise

from Chapter2.py import Array

class _MatrixElementNode(object):
    def __init__(self, col, value):
        self.col = col
        self.data = value
        self.next = None



class SparseMatrix(object):
    def __init__(self, row, col):
        self._numCols = col
        self._listOfRows = Array(row)

    def numRows(self):
        return len(self._listOfRows)

    def numCols(self):
        return self._numCols




    def __setitem__(self, ndxTuple, value):
        row = ndxTuple[0]
        col = ndxTuple[1]
        preNode = None
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            preNode = curNode
            curNode = curNode.next

        if curNode is not None and curNode.col == col:
            if value == 0:
                if curNode == self._listOfRows[row]:
                    self._listOfRows[row] = curNode.next
                else:
                    preNode.next = curNode.next
            else:
                curNode.data = value
        elif value != 0:
            newNode = _MatrixElementNode[col, value]
            newNode.next = curNode
            if curNode == self._listOfRows[row]:
                self._listOfRows[row] = newNode
            else:
                preNode.next = newNode

    def __add__(self, rhsMartrix):
        assert rhsMartrix.numCols == self.numCols and rhsMartrix.numRows == self.numRows, "dimen. doesn't match"

        newMatrix = SparseMatrix(self.numRows, self.numCols)

        for rowNo in range(self.numRows): # row is a linked list ADT
            curSelfNode = self._listOfRows[rowNo]
            curRhsMatrixNode = rhsMartrix[rowNo]
            while curSelfNode is not None and curRhsMatrixNode is not None:
                if curSelfNode.col == curRhsMatrixNode.col:
                    newMatrix[rowNo, curSelfNode.col].data = curSelfNode.data + curRhsMatrixNode.data
                elif curSelfNode.col < curRhsMatrixNode.col:
                    newMatrix[rowNo, curSelfNode.col].data = curSelfNode.data
                else:
                    newMatrix[rowNo, curRhsMatrixNode.col].data = curRhsMatrixNode.data
                curSelfNode = curSelfNode.next
                curRhsMatrixNode = curRhsMatrixNode.next
            while curSelfNode is not None:
                newMatrix[row, curSelfNode].data = curSelfNode.data
                curSelfNode = curSelfNode.next
            while curRhsMatrixNode is not None:
                newMatrix[row, curRhsMatrixNode].data = curRhsMatrixNode.data
                curRhsMatrixNode = curRhsMatrixNode.next




