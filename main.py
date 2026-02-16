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

my_task = Task("Create new task", "2026-02-17", 1)
my_task.mark_done()
print(my_task.is_completed)

print(my_task)