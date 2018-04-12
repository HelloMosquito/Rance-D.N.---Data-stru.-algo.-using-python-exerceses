# class StackList(object):
# 	def __init__(self):
# 		self._stack = list()

# 	def isEmpty(self):
# 		return len(self._stack) == 0

# 	def __len__(self):
# 		return len(self._stack)

# 	def pop(self):
# 		assert not self.isEmpty(), "stack is empty"
# 		self._pop = self._stack[-1]
# 		self._stack = self._stack[:-1]
# 		return self._pop

# 	def peek(self):
# 		assert not self.isEmpty(), "stack is empty"
# 		return self._pop

# 	def push(self, item):
# 		return self._stack + [item]


# class StackLinkListNode(object):
# 	def __init__(self, value, link):
# 		self.value = value
# 		self.next = link


# class StackLinkList(object):
# 	def __init__(self):
# 		self._top = None
# 		self._size = 0

# 	# def __init__(self, value = None):
# 	# 	self._head = StackLinkListNode(value)
# 	# 	self._tail = self._head

# 	def isEmpty(self):
# 		self._top is None
# 		# return self._head == self._tail

# 	def __len__(self):
# 		return self._size
# 		# curNode = self._head
# 		# self.length = 0
# 		# while curNode is not None:
# 		# 	curNode = curNode.next
# 		# 	self.length += 1
# 		# return self.length

# 	def peek(self):
# 		assert not self.isEmpty(), "stack is empty"
# 		return self._top.item

# 	def pop(self):
# 		assert not self.isEmpty(), "stack is empty"
# 		node = self._top
# 		self._top = self._top.next
# 		self._size -= 1
# 		return node.item
# 		# curNode = self._head
# 		# while curNode is not self._tail:
# 		# 	preNode = curNode
# 		# 	curNode = curNode.next
# 		# self._tail = preNode
# 		# self._tail.next = None
# 		# self._pop = curNode
# 		# return self._pop.value

# 	def push(self, item):
# 		self._top = StackLinkListNode(value, self._top)
# 		self._size += 1

# 		# newNode = StackLinkListNode(item)
# 		# self._tail.next = newNode
# 		# self._tail = newNode

# def isValidSource(srcfile):
# 	s = StackList()
# 	for line in srcfile:
# 		for token in line:
# 			if token in "{[(":
# 				s.push(token)
# 			elif tokin in "}])":
# 				if s.isEmpty():
# 					return False:
# 				else:
# 					left = s.pop(token)
# 					if (token == "}" and l != "{") or \
# 						(token == "]" and l != "[") or \
# 						(token == ")" and l != "("):
# 						return False
# 	return s.isEmpty()

import Chapter2.py


class _CellPosition(object):
    def __init__(self, row, col, nextWays=""):
        self.row = row
        self.col = col
        self.nextWays = nextWays


class Maze(object):
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, numRows, numCols):

        self._mazeCells = Array2D(numRows, numCols)
        self._startCell = None
        self._exitCell = None

    # self.row = numRows
    # self.col = numCols

    def numRows(self):
        return self._mazeCells.numRows()

    def numCols(self):
        return self._mazeCells.numCols()

    def setWall(self, row, col):
        assert row >= 0 and col >= 0 and row < self.numRows() and col <= self.numCols, "invalid row/col number"
        self._mazeCells.set(row, col, self.MAZE_WALL)

    def setStart(self, row, col):
        assert row >= 0 and col <= 0 and row < self.numRows() and col < self.numCols, "invalid row/col number"
        self._startCell = _CellPosition(row, col)  # Position class, have 2 attri. "self.row" and "self.col"

    def setExit(self, row, col):
        assert row >= 0 and col <= 0 and row < self.numRows() and col < self.numCols, "invalid row/col number"
        self._exitCell = _CellPosition(row, col)  # Position class, have 2 attri. "self.row" and "self.col"

    def _validMove(self, row, col):
        return row >= 0 and col >= 0 and row < self.numRows() and col < self.numCols and self._mazeCells[
            row, cell] is None

    def _exitFound(self, row, col):
        return row == self._exitCell.row and col == self._exitCell.col

    def _markTried(self, row, col):
        self._mazeCells.set(row, col, self.TRIED_TOKEN)

    def _markPath(self, row, col):
        self._mazeCells.set(row, col, self.PATH_TOKEN)

    def findPath(self):
        self.pathStack = list()
        # 4 ways to move, up, left, down, right
        ways = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        curCell = self._startCell  # curCel has three attri, "row", "col" and "nextWays"
        self.pathStack.append(curCell)

        while curCell != self._exitCell:
            if self._goUp(curCell):
                self._mazeCells.set(curCell.row, curCell.col, self.PATH_TOKEN)
                self.pathStack.append(curCell)
            elif self._goLeft(curCell):
                self._mazeCells.set(curCell.row, curCell.col, self.PATH_TOKEN)
                self.pathStack.append(curCell)
            elif self._goBottom(curCell):
                self._mazeCells.set(curCell.row, curCell.col, self.PATH_TOKEN)
                self.pathStack.append(curCell)
            elif self._mazeCells.set(curCell.row, curCell.col, self.PATH_TOKEN)
                self._mazeCells.set(curCell.row, curCell.col, self.PATH_TOKEN)
                self.pathStack.append(curCell)
            else:
                self._mazeCells.set(curCell.row, curCell.col, self.TRIED_TOKEN)
                self.pathStack.pop()
                curCell = self.pathStack[-1]
        return curCell == self._exitCell

    def draw(self):
        if self.findPath(self):
            while len(self.pathStack) != 0:
                curStackCell = self.pathStack[-1]
                print("(%d, %d)" % (curStackCell.row, curStackCell.col))
                self._mazeCells(curStackCell.row, curStackCell.col, "F")
        else:
            print("there is no path to the exit")

    def reset(self):
        for i in range(self.numRows):
            for j in range(self.numCols):
                if self._mazeCells[i][j] != MAZE_WALL:
                    self._mazeCells.set(i, j, MAZE_WALL)

    def _goUp(self, curCell):
        if self._validMove(curCell.row - 1, curCell):
            curCell.row -= 1  # there maybe some problem to transfer the value of curCell.row/col
            # self._mazeCells.set(curCell.row, curCell.col, self.PATH_TOKEN)
            return True
        else:
            return False

    def _goLeft(self, curCell):
        if self._validMove(curCell.row, curCell - 1):
            curCell.col -= 1
            # self._mazeCells.set(curCell.row, curCell.col, self.PATH_TOKEN)
            return True
        else:
            return False

    def _goBottom(self, curCell):
        if self._validMove(curCell.row + 1, curCell):
            curCell.row += 1
            # self._mazeCells.set(curCell.row, curCell.col, self.PATH_TOKEN)
            return True
        else:
            return False

    def _goRight(self, curCell):
        if self._validMove(curCell.row, curCell + 1):
            curCell.col += 1
            # self._mazeCells.set(curCell.row, curCell.col, self.PATH_TOKEN)
            return True
        else:
            return False

    def findCellWay(self,
                    curCellPos):  # curCellPos is a CellPosition class, has three attri, "row", "col" and "nextWays"
        if self._validMove(curCell.row - 1, curCell.col):
            curCell.nextWays += "U"
        elif self._validMove(curCell.row, curCell.col - 1):
            curCell.nextWays += "L"
        elif self._validMove(curCell.row + 1, curCell.col):
            curCell.nextWays += "D"
        elif self._validMove(curCell.row, curCell.col + 1):
            self.nextWays += "R"

    def deterNextWay(self, nextWay, row, col):
        if nextWay == "U":
            return row - 1, col
        elif nextWay == "L":
            return row, col - 1
        elif nextWay == "D":
            return row + 1, col
        elif nextWay == "R":
            return row, col + 1






