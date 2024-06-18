class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed


def main():
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.pop()
    print(s1.stack)

if __name__ == '__main__':
    main()