class MinStack:

    def __init__(self):
        self.container = [] # Setup container

    def push(self, val: int) -> None:
        self.container.append(val) # Push value to the container

    def pop(self) -> None:
        self.container.pop() # Pop value from the container

    def top(self) -> int:
        return self.container[-1] # Return the last push value

    def getMin(self) -> int:
        return min(self.container)
        
