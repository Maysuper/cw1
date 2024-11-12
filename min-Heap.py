# 2. Min-Heap for Loan Management (Prioritizing Due Dates)
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def get_min(self):
        return self.heap[0] if self.heap else None

    def remove_min(self):
        return heapq.heappop(self.heap) if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0