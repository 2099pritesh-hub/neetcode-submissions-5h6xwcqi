class StockSpanner:

    def __init__(self):
        self.stack = []
        self.price = []

    def next(self, price: int) -> int:
        i = len(self.stack) - 1
        res = 1
        while i >= 0:
            if self.price[i] <= price:
                res += self.stack[i]
                i -= self.stack[i]
            else:
                break
        self.price.append(price)
        self.stack.append(res)
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)