class arr_circular:
    def __init__(self,size_max):
        self.max_size = size_max
        self.body = [None]*size_max
        self.size = 0
        self.front = 0
    
    def enqueue(self, item):
        if self.size < self.max_size:
            rear = (self.front + self.size) % self.max_size
            self.body[rear] = item
            print(f"enqueue {item} at {self.size}")
            self.size += 1
        elif self.size >= self.max_size or item is None:
            print(f"enqueue None")
    
    def dequeue(self):
        if self.size != 0:
            item = self.body[self.front]
            print(f"dequeue {item}")
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return item
        else:
            print("dequeue None")
    
    def peek(self):
        if self.size != 0:
            print(f"peek {self.body[self.front]}")
            return self.body[self.front]
        else:
            print(f"peek {None}")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircLinkedList:
    def __init__(self):
        self.head = None
        self.back = None

    def enqueue(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is None:
            self.head = new_node
        else:
            self.back.next = new_node

        self.back = new_node   
        print(f"enqueue {data} in linked list")  

    def dequeue(self):
        if self.head is None:
            print(f"dequeue None")
            return
        elif self.head == self.back:
            Value = self.head.data
            self.head = self.back = None
            print(f"dequeue {Value}")
            return Value
        else:
            Value = self.head.data
            self.head = self.head.next
            self.back.next = self.head
            print(f"dequeue {Value}")
            return Value

    def peek(self):
        if self.head is None:
            print(f"peek None")
            return
        Value = self.head.data
        print(f"peek {Value}")
        return Value
           



MyList = arr_circular(10)
task_list = [
[None,"peek","peek None"],
[None,"dequeue","dequeue None"],

[10,"enqueue","enqueue 10 at 0"],
[20,"enqueue","enqueue 20 at 1"],
[30,"enqueue","enqueue 30 at 2"],
[40,"enqueue","enqueue 40 at 3"],
[50,"enqueue","enqueue 50 at 4"],

[None,"peek","peek 10"],

[None,"dequeue","dequeue 10"],
[None,"peek","peek 20"],

[60,"enqueue","enqueue 60 at 4"],
[70,"enqueue","enqueue 70 at 5"],
[80,"enqueue","enqueue 80 at 6"],
[90,"enqueue","enqueue 90 at 7"],
[100,"enqueue","enqueue 100 at 8"],
[110,"enqueue","enqueue 110 at 9"],

[120,"enqueue","enqueue None"],

[None,"peek","peek 20"],

[None,"dequeue","dequeue 20"],
[None,"dequeue","dequeue 30"],
[None,"dequeue","dequeue 40"],

[None,"peek","peek 50"],

[130,"enqueue","enqueue 130 at 7"],
[140,"enqueue","enqueue 140 at 8"],
[150,"enqueue","enqueue 150 at 9"],

[160,"enqueue","enqueue None"],

[None,"dequeue","dequeue 50"],
[None,"dequeue","dequeue 60"],
[None,"dequeue","dequeue 70"],
[None,"dequeue","dequeue 80"],
[None,"dequeue","dequeue 90"],
[None,"dequeue","dequeue 100"],
[None,"dequeue","dequeue 110"],
[None,"dequeue","dequeue 130"],
[None,"dequeue","dequeue 140"],
[None,"dequeue","dequeue 150"],

[None,"dequeue","dequeue None"],
[None,"peek","peek None"],

[200,"enqueue","enqueue 200 at 0"],
[None,"peek","peek 200"]
]

for task in task_list:
    if task[1] == "enqueue":
        MyList.enqueue(task[0])
    elif task[1] == "dequeue":
        MyList.dequeue()
    elif task[1] == "peek":
        MyList.peek()
    print(f"expected output is '{task[2]}'")

MyList = CircLinkedList()

task_list = [
[None,"peek","peek None"],
[None,"dequeue","dequeue None"],

[1,"enqueue","enqueue 1 in linked list"],
[2,"enqueue","enqueue 2 in linked list"],
[3,"enqueue","enqueue 3 in linked list"],

[None,"peek","peek 1"],
[None,"dequeue","dequeue 1"],

[None,"peek","peek 2"],
[4,"enqueue","enqueue 4 in linked list"],
[5,"enqueue","enqueue 5 in linked list"],

[None,"dequeue","dequeue 2"],
[None,"dequeue","dequeue 3"],

[None,"peek","peek 4"],

[6,"enqueue","enqueue 6 in linked list"],
[7,"enqueue","enqueue 7 in linked list"],

[None,"dequeue","dequeue 4"],
[None,"peek","peek 5"],

[None,"dequeue","dequeue 5"],
[None,"dequeue","dequeue 6"],

[None,"peek","peek 7"],

[8,"enqueue","enqueue 8 in linked list"],
[9,"enqueue","enqueue 9 in linked list"],

[None,"dequeue","dequeue 7"],

[None,"peek","peek 8"],

[None,"dequeue","dequeue 8"],
[None,"dequeue","dequeue 9"],

[None,"peek","peek None"],
[None,"dequeue","dequeue None"],

[10,"enqueue","enqueue 10 in linked list"],
[11,"enqueue","enqueue 11 in linked list"],

[None,"peek","peek 10"],

[None,"dequeue","dequeue 10"],

[None,"peek","peek 11"],

[None,"dequeue","dequeue 11"],

[None,"peek","peek None"],

[12,"enqueue","enqueue 12 in linked list"],
[13,"enqueue","enqueue 13 in linked list"],

[None,"peek","peek 12"],

[None,"dequeue","dequeue 12"],

[None,"peek","peek 13"]
]


for task in task_list:
    if task[1] == "enqueue":
        MyList.enqueue(task[0])
    elif task[1] == "dequeue":
        MyList.dequeue()
    elif task[1] == "peek":
        MyList.peek()
    print(f"expected output is '{task[2]}'")