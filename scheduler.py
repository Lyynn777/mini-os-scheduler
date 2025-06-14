from task import Task
from collections import deque

# ----- FCFS Scheduler -----
def fcfs_scheduler(task_list):
    task_list.sort(key=lambda t: t.arrival_time)
    current_time = 0
    for task in task_list:
        if current_time < task.arrival_time:
            current_time = task.arrival_time

        task.start_time = current_time
        task.end_time = current_time + task.burst_time
        current_time += task.burst_time

        print(f"{task.task_id} | Start: {task.start_time} | End: {task.end_time}")
    return task_list

# ----- Round Robin Scheduler -----
def round_robin_scheduler(task_list, quantum):
    task_list.sort(key=lambda t: t.arrival_time)
    queue = deque()
    time = 0
    index = 0
    completed = []

    while index < len(task_list) or queue:
        while index < len(task_list) and task_list[index].arrival_time <= time:
            queue.append(task_list[index])
            index += 1

        if not queue:
            time += 1
            continue

        current_task = queue.popleft()

        if current_task.start_time is None:
            current_task.start_time = time

        if current_task.remaining_time > quantum:
            time += quantum
            current_task.remaining_time -= quantum
            queue.append(current_task)
        else:
            time += current_task.remaining_time
            current_task.remaining_time = 0
            current_task.end_time = time
            completed.append(current_task)

        while index < len(task_list) and task_list[index].arrival_time <= time:
            queue.append(task_list[index])
            index += 1

    for task in completed:
        print(f"{task.task_id} | Start: {task.start_time} | End: {task.end_time}")
    return completed

# ----- Priority Scheduler -----
def priority_scheduler(task_list):
    task_list.sort(key=lambda t: (t.arrival_time, t.priority))
    current_time = 0
    completed = []

    while task_list:
        available_tasks = [task for task in task_list if task.arrival_time <= current_time]
        
        if not available_tasks:
            current_time += 1
            continue

        highest_priority_task = min(available_tasks, key=lambda t: t.priority)
        task_list.remove(highest_priority_task)

        highest_priority_task.start_time = current_time
        highest_priority_task.end_time = current_time + highest_priority_task.burst_time
        current_time += highest_priority_task.burst_time
        completed.append(highest_priority_task)

    for task in completed:
        print(f"{task.task_id} | Start: {task.start_time} | End: {task.end_time} | Priority: {task.priority}")
    return completed

# ----- Gantt Chart Visualizer -----
def print_gantt_chart(tasks):
    tasks.sort(key=lambda t: t.start_time)
    print("\nGantt Chart:")
    chart = ""
    timeline = ""

    for task in tasks:
        duration = task.end_time - task.start_time
        chart += "|" + f"{task.task_id}".center(duration * 2, "-")
        timeline += f"{str(task.start_time).ljust(duration * 2)}"
    chart += "|"
    timeline += str(tasks[-1].end_time)

    print(chart)
    print(timeline)

# ----- Main Demo -----
if __name__ == "__main__":
    # === FCFS ===
    tasks_fcfs = [
        Task("T1", 0, 5),
        Task("T2", 1, 3),
        Task("T3", 2, 1),
    ]
    print("=== FCFS Scheduling ===")
    fcfs_result = fcfs_scheduler(tasks_fcfs)
    print_gantt_chart(fcfs_result)

    # === Round Robin ===
    tasks_rr = [
        Task("T1", 0, 5),
        Task("T2", 1, 3),
        Task("T3", 2, 1),
    ]
    print("\n=== Round Robin Scheduling (Quantum = 2) ===")
    rr_result = round_robin_scheduler(tasks_rr, quantum=2)
    print_gantt_chart(rr_result)

    # === Priority Scheduling ===
    tasks_priority = [
        Task("T1", 0, 5, priority=2),
        Task("T2", 1, 3, priority=1),
        Task("T3", 2, 1, priority=3),
    ]
    print("\n=== Priority Scheduling ===")
    priority_result = priority_scheduler(tasks_priority)
    print_gantt_chart(priority_result)
