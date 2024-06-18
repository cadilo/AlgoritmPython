
class Queue():
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        return removed



def main():
    q1 = Queue()
    q1.push(1)
    q1.push(23)
    q1.push(732)
    q1.push(34)
    #q1.pop()
    q1.push("str")
    q1.pop()
    print(q1.queue)


if __name__ == '__main__':
    main()