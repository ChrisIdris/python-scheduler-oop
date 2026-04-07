"""
Session 2 — OOP Scheduler Refactor (Boilerplate)

Refactor your procedural scheduler into classes:
- Task: represents a single scheduled task
- Scheduler: manages loading, running, and executing tasks

Then write tests with pytest for both classes.
"""

from datetime import datetime
import time
import os


class Task:
    """Represents a single scheduled task."""
            
    def __init__(self, time_str, action, args, done=False):
        """Store the task's time, action, args, and done status."""
        self.time_str = time_str
        self.action = action
        self.args = args
        self.done = done

    def execute(self):
        """Execute this task's action.
        Supported: print, list_files, create_file
        Mark task as done after executing.
        """
        # TODO: move the execute_action logic here
        # use self.action and self.args
        # set self.done = True after executing
        if self.action == "print":
            print(self.args)

        elif self.action == "list_tasks":
            try:
                    with open(self.args,"r") as file:
                         for line in file:
                              print(line.strip())
            except FileNotFoundError:
                 print(f"file {self.args} not found.")

        elif self.action == "create_file":
            with open(self.args, "w") as f:
                f.write("Default entry")  # create an empty file
            print(f"Created file: {self.args}")

        else:
            print(f"Unknown action: {self.action}")

        self.done = True
        

    def is_due(self, current_time):
        """Check if this task should run at the given time.
        Returns True if time matches and task is not done.
        """
        # TODO: compare self.time_str with current_time, check self.done
        if self.time_str <= current_time and not self.done:
            return True
        return False

    def __str__(self):
        """Nice display: '09:00:05 | print Hello! [DONE]'"""
        # TODO: return a formatted string showing the task
        status = " [DONE]" if self.done else "[PENDING]"
        return f"Task time: {self.time_str} | Task action: {self.action} Input:{self.args}status: {status}"

    def __repr__(self):
        return f"Task('{self.time_str}', '{self.action}', '{self.args}')"


class Scheduler:
    """Manages loading and running scheduled tasks."""

    def __init__(self, filename):
        """Load tasks from the given file."""
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        """Load tasks from file."""
        tasks = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    line = line.strip()

                    # skip blank lines
                    if not line:
                        continue

                    # split the lines
                    parts = line.split(maxsplit=2)
                    
                    # ensure we have at least time and action
                    if len(parts) < 2:
                        continue

                    time = parts[0]
                    action = parts[1]
                    args = parts[2] if len(parts) == 3 else ""

                    tasks.append(Task(time, action, args))
        except FileNotFoundError:
            print(f"Warning: file '{self.filename}' not found.")
        
        return tasks

    def _get_current_time(self):
        """Return current time as HH:MM:SS string."""
        return datetime.now().strftime("%H:%M:%S")

    def check_and_execute(self):
        """Check all tasks against current time and execute any that are due.
        Returns the number of tasks executed this tick.
        """
        # TODO: loop through self.tasks
        # if task.is_due(current_time), call task.execute()
        # return count of executed tasks
        for task in self.tasks:
            if task.is_due(self._get_current_time()):
                task.execute()
        pass

    def all_done(self):
        """Return True if every task has been executed."""
        # TODO: check if all tasks are done
        for task in self.tasks:
            if not task.done:
                return False
        return True

    def run(self):
        """Main scheduler loop. Check tasks every second."""
        if not self.tasks:
            print("No tasks loaded. Exiting.")
            return

        print(f"Scheduler running with {len(self.tasks)} tasks... (Ctrl+C to stop)")
        try:
            while True:
                self.check_and_execute()
                if self.all_done():
                    print("\nAll tasks completed!")
                    break
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nScheduler stopped.")


# Run it
if __name__ == "__main__":
    scheduler = Scheduler("schedule.txt")
    scheduler.run()