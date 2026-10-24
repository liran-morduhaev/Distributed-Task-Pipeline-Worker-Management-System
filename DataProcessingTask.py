from BaseTask import BaseTask


class DataProcessingTask(BaseTask):
    def __init__(self, task_id: int, priority: int = 1, payload_size_mb: float = 0.0):
        super().__init__(task_id, priority)
        self.payload_size_mb = payload_size_mb

    def execute(self):
        if self.payload_size_mb > 1000:
            print(f"[Warning!] Task {self.task_id} Heavy payload detected ({self.payload_size_mb} MB). Processing in chunks...")
        else:
            print(f"Task {self.task_id}: Processing {self.payload_size_mb} MB of data...")
        self.is_completed = True
        return True

