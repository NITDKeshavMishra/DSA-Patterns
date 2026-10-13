from collections import deque

class StockSpanner:

    def __init__(self):
        self.st = deque()
        self.day = 0

    def next(self, price: int) -> int:
        while self.st and self.st[-1][0] <= price:
            self.st.pop()

        if not self.st:
            span = self.day + 1
        else:
            span = self.day - self.st[-1][1]

        self.st.append((price, self.day))
        self.day += 1

        return span