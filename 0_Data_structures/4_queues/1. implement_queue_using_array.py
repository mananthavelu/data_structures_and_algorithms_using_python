# First element is head
# Last element is Tail

""" 
Operations: Enqueue, Dequeue
Deque (Double ended queues): We can enqueue and dequeue from both the ends
Priority queue: When we insert an element in the queue; we assign the priority to each element and an element with highest priority is removed first
When more than one element shares the same priority; then the oldest element is removed first.
""" 
class Queue:
    def __init__(self, size = 5):
        self.array = [None for _ in range(size)]
        self.next_index = 0
        self.number_of_elements = 0
    
    def enqueue(self, new_element):
        self.array[self.next_index] = new_element
        self.next_index += 1
        self.number_of_elements += 1
        
    def dequeue(self):
        element_to_return = self.array[0]
        self.array = self.array[1:]
        self.next_index -= 1
        self.number_of_elements -=1
        return element_to_return

    def __repr__(self):
        print(self.array)
        return "Queue is printed"


new_queue = Queue()
new_queue.enqueue(5)
new_queue.enqueue(10)
new_queue.enqueue(15)
print(new_queue)
print(new_queue.next_index)
print(new_queue.number_of_elements)
print(new_queue.dequeue())
print(new_queue)
print(new_queue.next_index)
print(new_queue.number_of_elements)

