class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def print_queue(self):
        for item in self.queue:
            print(item)

    def add_string(self, string):
        self.queue.append(string)

    def dequeue_with_index(self, index):
        if not self.is_empty():
            return self.queue.pop(index)

# Create a queue object
my_queue = Queue()

while True:
    option = input("Enter the number of the option you would like to choose:\n1. Add a string to the queue\n2. Remove a string from the queue\n3. Print the queue\n4. Exit\n")
    if option == "1":
        string = input("Enter a string to add to the queue, then press enter: ")
        my_queue.add_string(string)
        print("String added to queue!")
    if option == "2":
        index = input("Enter the index of the string you would like to remove, then press enter(index starts at 0): ")
        my_queue.dequeue_with_index(index)
        print("String removed from queue!")
    if option == "3":
        print("Printing queue...")
        my_queue.print_queue()
    if option == "4":
        break

