class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # if self.storage[-1] is not None:
        #     self.storage[0] = item
        #     return
        # available = self.storage.count(None)
        # print(available)
        # while available > 0:
        #     for index in range(len(self.storage) - 1):
        #         if self.storage[index] is None:
        #             self.storage[index] = item
        #             available -= 1
        #             print(available)
        #             return

        #     self.storage.append(item)
        # print("Storage: ", self.storage, '\nCapacity: ', self.capacity)
        if self.current == 0:   # O(1)
            self.storage[0] = item  # O(1)
            self.current += 1  # O(1)
            return
        else:
            if self.current < self.capacity - 1:  # O(1)
                self.storage[self.current] = item  # O(1)
                self.current += 1  # O(1)
            else:
                self.storage[self.current] = item  # O(1)
                self.current = 0  # O(1)

    def get(self):
        current_values = []  # O(1)
        for item in self.storage:  # O(n)
            if item is not None:  # O(1)
                current_values.append(item)  # O(1)
        # print(current_values)
        return current_values  # O(1)
        # print("Storage: ", self.storage, '\nCapacity: ', self.capacity)


# buf = RingBuffer(3)
# buf.get()
# buf.append('m')
# buf.get()
# buf.append('3')
# buf.get()
# buf.append('kljh')
# buf.get()
# buf.append('65465')
# buf.get()
