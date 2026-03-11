import matplotlib.pyplot as plt
import timeit
import random
class arr_queue:
    def __init__(self):
        self.body = []
    def enqueue(self, item):
        if self.body is not None:
            self.body.insert(0,item)
        else:
            self.body = [item]
    def dequeue(self):
        return self.body.pop()

class list_queue:
    def __init__(self):
        self.list = None
    def enqueue(self, item):
        if self.list is None:
            self.list = SinglyLinkedList()
        self.list.append(item)
    def dequeue(self):
        if self.list is not None:
            tail = self.list.pop()
            return tail




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def pop(self):
        curr = self.head
        prev = None
        prev_2 = None
        while curr is not None:
            prev_2 = prev
            prev = curr
            curr = curr.next
        if prev_2 is not None:
            prev_2.next = None
        else:
            prev.next = None            
        return prev

    def get_tail(self):
        curr = self.head
        prev = None
        while curr is not None:
            prev = curr
            curr = curr.next
        return prev
    
def generate_queue_tasks(num_tasks=10000, enqueue_prob=0.7):
    """
    Generate a list of tasks for a queue.
    Each task is a tuple: ('enqueue', item) or ('dequeue',)
    """
    tasks = []
    for _ in range(num_tasks):
        if random.random() < enqueue_prob:
            # Generate a random item to enqueue
            item = random.randint(1, 100000)
            tasks.append(('enqueue', item))
        else:
            # Dequeue task
            tasks.append(('dequeue',))
    return tasks


# Generate 100 random task lists
task_lists = [generate_queue_tasks() for _ in range(100)]

# Function to run tasks on arr_queue
def run_arr_queue(tasks):
    q = arr_queue()
    for task in tasks:
        if task[0] == 'enqueue':
            q.enqueue(task[1])
        else:
            if q.body:  # Only dequeue if queue is not empty
                q.dequeue()

# Function to run tasks on list_queue
def run_list_queue(tasks):
    q = list_queue()
    for task in tasks:
        if task[0] == 'enqueue':
            q.enqueue(task[1])
        else:
            q.dequeue()

# Measure time for arr_queue
arr_times = []
list_times = []
total_list = 0
total_arr = 0
for task in task_lists:
    arr_times.append(timeit.timeit(lambda: run_arr_queue(task),number=1))
    total_arr += arr_times[-1]
    list_times.append(timeit.timeit(lambda: run_list_queue(task),number=1))
    total_list+= list_times[-1]


print(f"total time for array implementation is {total_arr:.2f} seconds")
print(f"total time for list implementation is {total_list:.2f} seconds")
runs = range(1, len(arr_times) + 1)

plt.plot(runs, arr_times, label="arr_queue")
plt.plot(runs, list_times, label="list_queue")

plt.xlabel("Run Number")
plt.ylabel("Execution Time (s)")
plt.title("Execution Time per Run for Queue Implementations")
plt.legend()
plt.show()