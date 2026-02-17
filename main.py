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

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None


class task_manager:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        if self.head is None or new_node.task.priority < self.head.task.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.task.priority <= new_node.task.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node 

    def print_all_tasks(self):
        current = self.head
        while current:
            print(current.task)
            current = current.next


manager = task_manager()

t1 = Task("Do Laundry", "2026-01-01", 3)     
t2 = Task("Submit Final Project", "2026-02-01", 1) 
t3 = Task("Buy Groceries", "2026-01-02", 2)   


print("Adding tasks...")
manager.add_task(t1) 
manager.add_task(t2) 
manager.add_task(t3) 


print("\n--- Sorted by Priority ---")
manager.print_all_tasks()