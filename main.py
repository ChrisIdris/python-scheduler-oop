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
        # TODO: store attributes on self
        pass

    def execute(self):
        """Execute this task's action.
        Supported: print, list_files, create_file
        Mark task as done after executing.
        """
        # TODO: move the execute_action logic here
        # use self.action and self.args
        # set self.done = True after executing
        pass

    def is_due(self, current_time):
        """Check if this task should run at the given time.
        Returns True if time matches and task is not done.
        """
        # TODO: compare self.time_str with current_time, check self.done
        pass

    def __str__(self):
        """Nice display: '09:00:05 | print Hello! [DONE]'"""
        # TODO: return a formatted string showing the task
        pass

    def __repr__(self):
        return f"Task('{self.time_str}', '{self.action}', '{self.args}')"


class Scheduler:
    """Manages loading and running scheduled tasks."""

    def __init__(self, filename):
        """Load tasks from the given file."""
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        """Read the schedule file and return a list of Task objects.
        Each line format: HH:MM:SS command argument
        Skip blank lines and handle missing file.
        """
        tasks = []
        # TODO: open self.filename, parse each line
        # create Task objects instead of dicts
        # handle FileNotFoundError
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
        pass

    def all_done(self):
        """Return True if every task has been executed."""
        # TODO: check if all tasks are done
        pass

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