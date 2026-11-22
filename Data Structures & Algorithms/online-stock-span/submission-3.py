class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        i = len(self.stack) - 1
        span = 1
        while i >= 0:
            if self.stack[i][0] <= price:
                span += self.stack[i][1]
                i -= self.stack[i][1]
            else:
                break
        self.stack.append([price, span])
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)