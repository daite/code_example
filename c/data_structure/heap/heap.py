#!/usr/bin/env python3

class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def arrange(self, idx):
        while idx // 2 > 0:
            if self.heap[idx] < self.heap[idx//2]:
                self.heap[idx], self.heap[idx//2] = self.heap[idx//2], self.heap[idx]
            idx //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)
    
    def miniindex(self, idx):
        if idx * 2 + 1 > self.size:
            return idx * 2
        elif self.heap[idx*2] < self.heap[idx*2+1]:
            return idx * 2
        else:
            return idx * 2 + 1
    
    def sink(self, idx):
        while idx*2 <= self.size: #
            mi = self.miniindex(idx)
            if self.heap[idx] > self.heap[mi]:
                self.heap[idx], self.heap[mi] = self.heap[mi], self.heap[idx]
            idx = mi

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item


h = Heap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)

for _ in range(10):
    print(h.pop(), end='\t')
