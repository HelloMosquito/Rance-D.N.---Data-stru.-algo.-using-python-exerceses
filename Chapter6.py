class BagListNode(object):
    def __init__(self):
        self.data = None
        self.next = None

    class Bag(object):
    def __init__(self):
        self._head = None
        self._size = 0
        # self.data = None
        # self.next = None

    # class BagLinkList(object):
    # def __init__(self):
    # 	self.head = None
    # 	self.item = Bag()

    def __len__(self):
        return self._size
        # curNode = head
        # size = 0
        # while curNode is not None:
        # 	curNode = curNode.next
        # 	size += 1
        # return size

    def __contains__(self, item):
        curNode = self.head
        while curNode is not None and item != curNode.data:
            curNode = curNode.next
        return curNode is not None
        # return item == curNode.data

    def add(self, item):
        newNode = BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    def remove(self, item):
        curNode = self._head
        while curNode is not None and item != curNode.data:
            preNode = curNode
            curNode = curNode.next

        if curNode is not None:
            self._size -= 1
            if curNode is head:
                self._head = self._head.next
            else:
                preNode.next = curNode.next
            return curNode.data
        else:
            # raise "no such an item"
            raise