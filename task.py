class Task:
    def __init__(self, title):
        self.title = title
        self.status = "Pending"

    def __str__(self):
        return f"{self.title} - {self.status}"
    
    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status
        }