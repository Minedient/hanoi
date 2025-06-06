class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def size(self):
        return len(self.items)
    
class Stack:

    def __init__(self):
        self.__stack = []

    def push(self, pole):
        self.__stack.append(pole)

    def pop(self):
        if not self.__stack:
            raise IndexError("pop from empty stack")
        return self.__stack.pop()

    def peek(self):
        if not self.__stack:
            return None
        return self.__stack[-1]

    def is_empty(self):
        return len(self.__stack) == 0

    def size(self):
        return len(self.__stack)
    
# Question 1: 打印隊列中所有的元素，注意打印完成後隊列的元素順序不變。
def print_queue(queue: Queue):
    pass

# Question 2: 初始化隊列，將頭n個單數加入到隊列當中。
def initialize_odd(queue: Queue, n: int):
    pass

# Question 3: 把隊列的元素反轉，即第一個元素變成最尾，最尾的元素變成第一個。
def reverse_queue(queue: Queue):
    pass

# Question 4 (Adv): 把隊列中頭k個元素反轉
def reverse_k_elements(queue: Queue, k: int):
    pass

if __name__ == "__main__":
    q = Queue()
    
    # Test Question 1
    print("Question 1: Print Queue")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print("Original Queue:")
    print("1 2 3 4 5")
    print("You should see:")
    print("1 2 3 4 5")
    print("Actual output:")
    print_queue(q)
    print("\n")

    # Test Question 2
    print("Question 2: Initialize Queue with first n odd numbers")
    q = Queue()
    initialize_odd(q, 7)
    print("Original Queue:")
    print("1 3 5 7 9 11 13")
    print("You should see:")
    print("1 3 5 7 9 11 13")
    print("Actual output:")
    print_queue(q)
    print("\n")

    # Test Question 3
    print("Question 3: Reverse Queue")
    q = Queue()
    initialize_odd(q, 7)
    print("Original Queue:")
    print("1 3 5 7 9 11 13")
    print("You should see:")
    print("13 11 9 7 5 3 1")
    print("Actual output:")
    reverse_queue(q)
    print_queue(q)
    print("\n")

    # Test Question 4 (Adv)
    print("Question 4: Reverse first k elements in Queue")
    q = Queue()
    initialize_odd(q, 7)
    print("Original Queue:")
    print("1 3 5 7 9 11 13")
    print("You should see:")
    print("5 3 1 7 9 11 13")
    print("Actual output:")
    reverse_k_elements(q, 3)
    print_queue(q)