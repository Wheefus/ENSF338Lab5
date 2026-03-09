# Exercise 3 – stack performance [1.5 pts]
# • In this exercise you will analyze the performance of different stack
# implementations

# 1. Implement a stack which internally uses Python arrays. push() must
# append an element at the tail, and pop() must remove an element
# from the tail [0.3 pts]
push_array = []
def push_array_stack(element):
    push_array.append(element)
def pop_array_stack():
    if len(push_array) == 0:
        raise IndexError("Stack is empty")
    return push_array.pop()


# 2. Implement a stack which internally uses a singly-linked list. push()
# must add an element at the head, and pop() must remove the head
# element [0.3 pts]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("Stack is empty")
        data = self.head.data
        self.head = self.head.next
        return data


# Exercise #3 /2
# 3. Write a function which generates random lists of 10000 tasks. Each
# task is either a push w/ probability 0.7, or a pop w/ probability 0.3
# [0.3 pts]
import random
def generate_random_tasks(num_tasks=10000):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:
            tasks.append(('push', random.randint(1, 100)))
        else:
            tasks.append(('pop', None))
    return tasks




# 4. Measure the performance of both implementations on 100 such
# lists of tasks using timeit and print the results [0.3 pts]
import timeit
def measure_performance(tasks):
    array_time = timeit.timeit(lambda: execute_tasks_array(tasks), number=1)
    linked_list_time = timeit.timeit(lambda: execute_tasks_linked_list(tasks), number=1)
    return array_time, linked_list_time
def execute_tasks_array(tasks):
    for task in tasks:
        if task[0] == 'push':
            push_array_stack(task[1])
        else:
            try:
                pop_array_stack()
            except IndexError:
                pass
def execute_tasks_linked_list(tasks):
    stack = LinkedListStack()
    for task in tasks:
        if task[0] == 'push':
            stack.push(task[1])
        else:
            try:
                stack.pop()
            except IndexError:
                pass


# 5. Plot the distribution of times (distributions for each implementation
# should be overlayed in the same plot; make sure to use consistent
# ranges) and discuss the results [0.3 pts]
import matplotlib.pyplot as plt
def plot_performance(array_times, linked_list_times):
    plt.hist(array_times, bins=20, alpha=0.5, label='Array Stack')
    plt.hist(linked_list_times, bins=20, alpha=0.5, label='Linked List Stack')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Performance of Stack Implementations')
    plt.legend()
    plt.show()
def main():
    array_times = []
    linked_list_times = []
    for _ in range(100):
        tasks = generate_random_tasks()
        array_time, linked_list_time = measure_performance(tasks)
        array_times.append(array_time)
        linked_list_times.append(linked_list_time)
    plot_performance(array_times, linked_list_times)


main()

