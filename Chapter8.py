# class Queue(object):
# 	def __init__(self):
# 		self._queue = list()

# 	def isEmpty(self):
# 		return len(self._queue) == 0

# 	def __len__(self):
# 		return len(self._queue)

# 	def enqueue(self, item):
# 		self._queue.append(item)

# 	def dequeue(self):
# 		assert not self.isEmpty(), "queue is empty, cannot dequeue from it"
# 		return self._queue.pop(0)
# 		# del self._queue[0]
# 		# return self._queue



# class CircleQueue(object):
# 	def __init__(self, size):
# 		self._cirqueue = Array(size)
# 		self._front = 0
# 		self._back = 0
# 		self._count = 0
# 		self._maxSize = size

# 	def isEmpty(self):
# 		return self._count == 0

# 	def isFull(self):
# 		return self._count == len(self._cirqueue)

# 	def __len__(self):
# 		return self._count

# 	def enqueue(self, item):
# 		assert not self.isFull, "Queue is full"
# 		self._back = (self._back + 1) % self._maxSize
# 		self._cirqueue[self._back] = item
# 		self._count += 1

# 	def dequeue(self):
# 		assert not self.isEmpty, "Queue is empty"
# 		dequeueItem = self._cirqueue[self._front]
# 		self._front = (self._front + 1) % self._maxSize
# 		self._count -= 1
# 		return dequeueItem


# class LinkedQueueNode(object):
# 	def __init__(self, value = None):
# 		self.value = value
# 		self.next None

# class LinkedQueue(object):
# 	def __init__(self):
# 		self._head = LinkedQueueNode()
# 		self._tail = self._head
# 		self._count = 0

# 	def isEmpty(self):
# 		return self._head == None

# 	def __len__(self):
# 		return self.count

# 	def enqueueD(self, item):
# 		newNode = LinkedQueueNode(item)
# 		if self.isEmpty():
# 			self._head = newNode
# 			# self._tail = newNode
# 		else:
# 			self._tail.next = newNode
# 		self._tail = newNode
# 		self._count += 1

# 	def dequeue(self):
# 		assert not self.isEmpty(), "queue is Empty, cannot dequeue from it "
# 		dequeueNode = self._head
# 		if self._head is self._tail:
# 			self._tail.next	= None
# 		self._head = self._head.next
# 		self._count -= 1
# 		return dequeueNode.value


# class PrioQueue(object):
# 	def __init__(self):
# 		self._prioQueue = list()

# 	def isEMpty(self):
# 		return len(self) == 0

# 	def __len__(self):
# 		return len(self._prioQueue)

# 	def enqueue(self, item, priority):	# order the list when enqueue
# 		newNode = PrioQueueNode(item, priority)
# 		if self.isEmpty:
# 			self._prioQueue[0] = newNode
# 		else:
# 			for i in range(len(self)):
# 				if newNode.priority < self._priority[i].priority:
# 					self._priority.insert(i, newNode)

# 	def dequeue(self):
# 		assert self.isEMpty(), "cannot dequeue from an empty queue"
# 		return self.priority.pop(0)


# class PrioQueueNode(object):
# 	def __init__(self, value, priority):
# 		self._value = value
# 		self._priority = priority

class BPriorityQueue(object):
	def __init__(self, numLevels):
		self._prioLevels = Array(numLevels)
		self._size = 0
		for i in range(numLevels):
			self._prioLevels[i] = Queue()

	def isEmpty(self):
		return len(self) == 0

	def __len__(self):
		for i in range(len(self._prioLevels)):
			self._size += len(self._prioLevels[i])
		return self._size


	def enqueue(self, item, priority):
		assert priority >= 0 and priority < len(self._prioLevels), "invalid priority"
		self._prioLevels[priority].enqueue(item)

	def dequeue(self):
		assert not self.isEmpty, "cannot dequeue from an empty queue"
		i = 0
		p = len(self._prioLevels)
		while i <= p and not self._prioLevels[i].isEmpty():
			i += 1
		return self._prioLevels[i].dequeue()











# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.enqueue(6)
# q.enqueue(7)

# print(q.isEmpty())
# print(q.dequeue())
# print(len(q))
# print(q._queue)