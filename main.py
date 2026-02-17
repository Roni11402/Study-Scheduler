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
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_all_tasks(self):
        current = self.head
        while current:
            print(current.task)
            current = current.next


manager = task_manager()
t1 = Task("Complete project", "2026-02-21", 1)
t2 = Task("Submit Algebra paper", "2026-03-01", 2)
manager.add_task(t1)
manager.add_task(t2)
manager.print_all_tasks()