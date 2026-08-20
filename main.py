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

    def peek(self):
        if not self.heap:
            return None
        else:
            return self.heap[0]

    def save_to_file(self, file_name):
         with open(file_name + ".csv", "w") as file:
             for task in self.heap:
                 line_to_write = task.to_csv() + "\n"
                 file.write(line_to_write)

    def load_from_file(self, file_name):
         with open(file_name + ".csv", "r") as file:
             for line in file:
                 clean_text = line.strip()
                 data = clean_text.split(',')
                 new_task = Task(data[0], data[1], int(data[2]))
                 new_task.is_completed = (data[3] == "True")
                 self.add_task(new_task)

