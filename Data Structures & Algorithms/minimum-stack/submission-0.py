class MinStack:

    def __init__(self):
        self.min_ele = float('inf')
        self.arr = []
        self.min_arr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min_arr:
            self.min_arr.append(val)
        else:
            self.min_arr.append(min(self.min_arr[-1], val))
        
    def pop(self) -> None:
        self.min_arr.pop()
        return self.arr.pop()
        
    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min_arr[-1]
        
