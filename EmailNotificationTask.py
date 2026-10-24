from BaseTask import BaseTask

class EmailNotificationTask(BaseTask):
    def __init__(self, task_id: int, recipient_email: str, subject: str, priority: int = 1):
        super().__init__(task_id, priority)
        self.recipient_email = recipient_email
        self.subject = subject

        if self.recipient_email != '@':
            raise ValueError(f"Invalid email address {self.recipient_email}")


    def execute(self):
            print(f"Sending notification to {self.recipient_email} - Subject: {self.subject}")
            self.is_completed = True
            return True
