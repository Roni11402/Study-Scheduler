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

    def remove_task(self, title):
         if self.head is None:
             return
         if self.head.task.title == title:
            self.head = self.head.next
            return
         else:
             current = self.head
             while current.next:
                 if current.next.task.title == title:
                     current.next = current.next.next
                     return
                 else:
                     current = current.next
                     

    def print_all_tasks(self):
        current = self.head
        while current:
            print(current.task)
            current = current.next

    def save_to_file(self, file_name):
        with open(file_name + ".csv", "w") as file:
            current = self.head
            while current:
                line_to_write = current.task.to_csv() + "\n"
                file.write(line_to_write)
                current = current.next

    def load_from_file(self, file_name):
        with open(file_name + ".csv", "r") as file:
            for line in file:
                clean_text = line.strip()
                data = clean_text.split(',')
                new_task = Task(data[0], data[1], int(data[2]))
                new_task.is_completed = (data[3] == "True")
                self.add_task(new_task)
                           

manager = task_manager()

print("--- Loading from file... ---")
manager.load_from_file("my_tasks")
manager.print_all_tasks()

print("\n--- Adding a new task ---")
manager.add_task(Task("Learn Python", "2026-03-01", 1))
manager.save_to_file("my_tasks") 

print("Saved! Now close the program and run it again.")