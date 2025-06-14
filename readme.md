![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)



# Mini OS-Level CPU Task Scheduler

A simulation of classic CPU scheduling algorithms using Python. Built to visualize and understand core Operating System concepts like FCFS, Round Robin, and Priority Scheduling.

---

## Features

- FCFS (First-Come-First-Serve)
- Round Robin with configurable quantum
- Non-Preemptive Priority Scheduling
- Gantt Chart visualization in the terminal
- Modular design for future extensions (CLI/GUI ready)

---

## Project Structure

├── task.py # Task class with attributes like arrival_time, burst_time, priority

├── scheduler.py # Main logic for all scheduling algorithms + Gantt chart

└── README.md # Project documentation

---

## How to Run

### Prerequisites

- Python 3.6 or higher

### Steps

1. Clone or download this repository.
2. Run the simulation:

```bash
python scheduler.py
```
---

## Sample Output

=== FCFS Scheduling ===

T1 | Start: 0 | End: 5

T2 | Start: 5 | End: 8

T3 | Start: 8 | End: 9

Gantt Chart:
|--T1--|--T2--|--T3--|

0          5              8           9   

---

## Future Scope
- Add Preemptive Priority and Shortest Job First (SJF) scheduling

- Generate performance metrics: Turnaround Time, Waiting Time

- Add CLI interface using argparse

- Add GUI using Tkinter

- Build a web-based simulator using Flask or React

### Author
Pragya M S
(Built as a part of Operating Systems concept revision)

## License
This project is licensed under the MIT License. You are free to fork and build upon it.
