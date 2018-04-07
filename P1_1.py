class Counter(object):
    def __init__(self):
        self.count = 0

    def press(self):
        self.count += 1
        print("the No is %d"%self.count)


class Reset(Counter):
    def __index__(self):
        pass
    def press(self):
        self.count = 0
        print("reset the No as %d"%self.count)

c = Counter()
# c.press()
for i in range(5):
    c.press()
r = Reset()
r.press()
