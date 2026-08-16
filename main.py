class Task:
    def __init__ (self, title, deadline, priority):
        self.title = title
        self.deadline = deadline
        self.priority = priority
        self.is_completed = False

    def mark_done(self):
        self.is_completed = True
        print("Well done! Task marked as completed.")

    def __str__(self):
        return f"Task: {self.title}, Deadline: {self.deadline}, Priority: {self.priority}, Completed: {self.is_completed}"

    def to_csv(self):
        return f"{self.title},{self.deadline},{self.priority},{self.is_completed}"

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None


# class task_manager:
#     def __init__(self):
#         self.head = None

#     def add_task(self, task):
#         new_node = Node(task)
#         if self.head is None or new_node.task.priority < self.head.task.priority:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next and current.next.task.priority <= new_node.task.priority:
#                 current = current.next
#             new_node.next = current.next
#             current.next = new_node

#     def remove_task(self, title):
#          if self.head is None:
#              return
#          if self.head.task.title == title:
#             self.head = self.head.next
#             return
#          else:
#              current = self.head
#              while current.next:
#                  if current.next.task.title == title:
#                      current.next = current.next.next
#                      return
#                  else:
#                      current = current.next
                     

#     def print_all_tasks(self):
#         current = self.head
#         while current:
#             print(current.task)
#             current = current.next

#     def save_to_file(self, file_name):
#         with open(file_name + ".csv", "w") as file:
#             current = self.head
#             while current:
#                 line_to_write = current.task.to_csv() + "\n"
#                 file.write(line_to_write)
#                 current = current.next

#     def load_from_file(self, file_name):
#         with open(file_name + ".csv", "r") as file:
#             for line in file:
#                 clean_text = line.strip()
#                 data = clean_text.split(',')
#                 new_task = Task(data[0], data[1], int(data[2]))
#                 new_task.is_completed = (data[3] == "True")
#                 self.add_task(new_task)

class HeapTaskManager:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index-1)//2

    def left_child(self,index):
        return 2*index + 1

    def right_child(self,index):
        return 2*index + 2

    def heapify_up(self, index):
        while index > 0 and self.heap[index].priority < self.heap[self.parent(index)].priority:
            p_index = self.parent(index)
            self.heap[index], self.heap[p_index] = self.heap[p_index], self.heap[index]
            index = p_index

    def add_task(self, task):
        self.heap.append(task)
        self.heapify_up(len(self.heap) - 1)

    def pop_task(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_task = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_task

    def heapify_down(self,index):
        while self.left_child(index) < len(self.heap):
            smaller_child = self.left_child(index)
            if self.right_child(index) < len(self.heap) and self.heap[self.right_child(index)].priority < self.heap[smaller_child].priority:
                smaller_child = self.right_child(index)
            if self.heap[index].priority <= self.heap[smaller_child].priority:
                break
            else:
                self.heap[index], self.heap[smaller_child] = self.heap[smaller_child], self.heap[index]
                index = smaller_child



manager = HeapTaskManager()
manager.add_task(Task("Do Laundry", "2026-08-10", 5))
manager.add_task(Task("Submit Algebra Paper", "2026-08-12", 1))
manager.add_task(Task("Buy Groceries", "2026-08-09", 3))
manager.add_task(Task("Call Parents", "2026-08-16", 2))
manager.add_task(Task("Pay Bills", "2026-08-20", 4))
print("Extracting tasks by priority:")
print("-" * 30)
popped_task = manager.pop_task()
while popped_task is not None:
    print(popped_task)
    popped_task = manager.pop_task()