from abc import ABC, abstractmethod

class BaseTask(ABC):
    PRIORITY = {1,2,3,4,5}
    def __init__(self, task_id, priority, is_completed = False):
        self.task_id = task_id
        self.priority = priority
        self.is_completed = is_completed

    @abstractmethod
    def execute(self):
        pass


    def __repr__(self):
        return f'Task [{self.task_id}] (Priority: {self.priority})'

    def __lt__(self, other):
        return self.priority < other.priority