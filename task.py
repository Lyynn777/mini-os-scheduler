class Task:
    def __init__(self, task_id, arrival_time, burst_time, priority=0):
        self.task_id = task_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.start_time = None
        self.end_time = None

    def __repr__(self):
        return (f"Task({self.task_id}, AT={self.arrival_time}, "
                f"BT={self.burst_time}, P={self.priority})")
