from ResourceCapacityException import ResourceCapacityException

class WorkerNode:
    def __init__(self, node_id, max_capacity, queue = None):
        self.node_id = node_id
        self.max_capacity = max_capacity
        self._queue = list(queue) if queue is not None else []

    def __len__(self):
        return len(self._queue)

    def __iter__(self):
        sorted_tasks = sorted(self._queue, reverse=True)
        return iter(sorted_tasks)

    def assign_task(self, task):
        if len(self._queue) >= self.max_capacity:
            raise ResourceCapacityException(f"Node {self.node_id} has exceeded max capacity ({self.max_capacity}).")
        self._queue.append(task)

    def process_all(self):
        completed_tasks = 0
        failed_tasks = 0
        for task in self._queue:
            success = task.execute()
            if success:
                completed_tasks += 1
            else:
                failed_tasks += 1
        self._queue.clear()
        return {
            "node_id": self.node_id,
            "completed_tasks": completed_tasks,
            "failed_tasks": failed_tasks
        }