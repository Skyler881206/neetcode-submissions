class MinStack:

    def __init__(self):
        self.stack_container = [] # Setup container
        self.min_container = []

    def push(self, val: int) -> None:
        self.stack_container.append(val) # Push value to the container
        val = min(val, self.min_container[-1] if self.min_container else val)
        self.min_container.append(val)

    def pop(self) -> None:
        self.stack_container.pop() # Pop value from the container
        self.min_container.pop()

    def top(self) -> int:
        return self.stack_container[-1] # Return the last push value

    def getMin(self) -> int:
        return self.min_container[-1]
        
