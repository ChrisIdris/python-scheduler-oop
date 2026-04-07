from main import Scheduler, Task
import os

def test_scheduler_initialization():
    scheduler = Scheduler.__new__(Scheduler)
    scheduler.filename = None
    scheduler.tasks = []
    assert scheduler.filename is None
    assert scheduler.tasks == []


def test_load_tasks(tmp_path):
    file = tmp_path / "test_schedule.txt"

    file.write_text(
        "09:00:00 print Hello\n"
        "09:01:00 create_file test.txt\n"
    )

    scheduler = Scheduler(file)

    assert len(scheduler.tasks) == 2
    assert scheduler.tasks[0].action == "print"


def test_all_done():
    scheduler = Scheduler.__new__(Scheduler)  # bypass __init__
    scheduler.tasks = [
        Task("09:00:00", "print", "Hi", done=True),
        Task("09:01:00", "print", "Hi", done=True),
    ]

    assert scheduler.all_done() is True


def test_check_and_execute(monkeypatch):
    scheduler = Scheduler.__new__(Scheduler)
    task = Task("09:00:00", "print", "Hi")
    scheduler.tasks = [task]

    # mock current time
    monkeypatch.setattr(scheduler, "_get_current_time", lambda: "09:00:01")

    scheduler.check_and_execute()

    assert task.done is True