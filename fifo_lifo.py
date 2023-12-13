class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
       return self.items == []

    def push_to_stack(self, item):
        self.items.append(item)

    def remove_from_stack(self):
        return self.items.pop()

    def stack_size(self):
        return len(self.items)


class My_Queue():
    def __init__(self):
        self.queue = []

    def add_to_queue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def is_empty(self):
        return self.queue == []

my_queue = My_Queue()
print(my_queue.is_empty())
my_queue.add_to_queue(42)
my_queue.add_to_queue(43)
print(my_queue.is_empty())
print(my_queue.dequeue())
print(my_queue.dequeue())


