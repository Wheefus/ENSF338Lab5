import random
import timeit
class PQ_merge:
    def __init__(self):
        self.body = []
    def enqueue(self,item,priority):
        if self.body is not None:
            self.body.append([priority,item])
            self.body = mergesort(self.body)
        else:
            self.body = [[priority,item]]
    def dequeue(self):
        output = self.body.pop()
        return output

class PQ_insert:
    def __init__(self):
        self.body = []
    def enqueue(self,item,priority):
        for i in range(len(self.body)):
            if(priority >= self.body[i][0]):
                if self.body is not None:
                    self.body.insert(i, [priority,item])
                else:
                    self.body =[[priority,item]]
    def dequeue(self):
        output = self.body.pop(0)
        return output

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]
    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i][0] <= R[j][0]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergesort(arr, l = 0, r = None):
    if r == None:
        r =  len(arr)-1
    if l < r:
        m = l + (r - l) // 2
        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        merge(arr, l, m, r)

def generate_tasks(num_tasks=1000, enqueue_prob=0.7):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < enqueue_prob:
            # Generate a random item and priority
            item = random.randint(1, 10000)
            priority = random.randint(1, 100)
            tasks.append(('enqueue', item, priority))
        else:
            # Dequeue task
            tasks.append(('dequeue',))
    return tasks

task_lists = [generate_tasks() for _ in range(100)]

# Function to run tasks on PQ_merge
def run_merge(tasks):
    pq = PQ_merge()
    for task in tasks:
        if task[0] == 'enqueue':
            pq.enqueue(task[1], task[2])
        else:
            if pq.body:  # Only dequeue if not empty
                pq.dequeue()

# Function to run tasks on PQ_insert
def run_insert(tasks):
    pq = PQ_insert()
    for task in tasks:
        if task[0] == 'enqueue':
            pq.enqueue(task[1], task[2])
        else:
            if pq.body:  # Only dequeue if not empty
                pq.dequeue()

# Measure time for PQ_merge
t_merge = timeit.timeit(
    lambda: [run_merge(tasks) for tasks in task_lists],
    number=1
)

# Measure time for PQ_insert
t_insert = timeit.timeit(
    lambda: [run_insert(tasks) for tasks in task_lists],
    number=1
)

print(f"Total time for PQ_merge on 100 lists: {t_merge:.4f} s")
print(f"Total time for PQ_insert on 100 lists: {t_insert:.4f} s")

# the inserting the elements in the correct spot implementation is faster
# as mergsort is O(n log n) while a simple search + insertion is O(n)
# which is smaller for large values