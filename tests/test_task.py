from main import Task


def test_task_initialization():
    task = Task("09:00:00", "print", "Hello")

    assert task.time_str == "09:00:00"
    assert task.action == "print"
    assert task.args == "Hello"
    assert task.done is False


def test_task_is_due_true():
    task = Task("09:00:00", "print", "Hello")

    assert task.is_due("09:00:01") is True


def test_task_is_due_false_if_done():
    task = Task("09:00:00", "print", "Hello", done=True)

    assert task.is_due("09:00:01") is False


def test_task_execute_print(capsys):
    task = Task("09:00:00", "print", "Hello")

    task.execute()

    captured = capsys.readouterr()
    assert "Hello" in captured.out
    assert task.done is True


def test_task_str():
    task = Task("09:00:00", "print", "Hello")

    result = str(task)

    assert "09:00:00" in result
    assert "print" in result
    assert "[PENDING]" in result