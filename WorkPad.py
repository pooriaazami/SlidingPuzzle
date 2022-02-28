from queue import PriorityQueue

queue = PriorityQueue()

queue.put((10, 'C++'))
queue.put((1, 'JAVA'))
queue.put((2, 'Python'))
queue.put((3, 'C'))
queue.put((4, 'Julia'))

while not queue.empty():
    item = queue.get()
    print(item)
