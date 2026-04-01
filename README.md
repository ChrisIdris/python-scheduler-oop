# Task Scheduler - OOP

A Python program that reads scheduled tasks from a file and executes them at the right time. But this time, it's refactored in OOP.

## File format

Each line in `schedule.txt` follows this format:
```
HH:MM:SS command argument
```

Three supported commands:

| Command | Argument | Example |
|---|---|---|
| `print` | Message to print | `09:00:05 print Good morning!` |
| `list_files` | Directory path | `09:00:10 list_files .` |
| `create_file` | Filename | `09:00:15 create_file log.txt` |

## Sample schedule.txt
```
09:00:05 print Good morning!
09:00:10 create_file log.txt
09:00:15 list_files .
09:00:20 print All done!
```

## How to run

1. Create your `schedule.txt` with tasks set a few seconds from now
2. Run the scheduler:
```
python scheduler.py
```

3. Press `Ctrl+C` to stop

## What to implement

Implement the scheduler just as the coursework from yesterday, but with OOP instead of procedural programming.
Complete the two `classes` and their relative methods.

- `Task` — Represents a single scheduled task
- `Scheduler` — Manages loading and running scheduled tasks

## Tests with Pytest

- Create tests under the `tests` folder for the `Task` class
- Create tests under the `tests` folder for the `Scheduler` class