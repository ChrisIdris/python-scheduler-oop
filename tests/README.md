# Tests

This folder will contain all the tests you write for the project, written using [**pytest**](https://docs.pytest.org/).

Run from your command line with `pytest`.

## Test File Naming

Pytest automatically discovers test files that match one of these naming patterns:

- **`test_*.py`** ← **recommended**
- **`*_test.py`**

> **Tip:** Always start your test files with `test_` for better consistency.

## Test Function and Class Naming

Pytest collects tests from:

- Functions whose names start with `test_`
- Methods inside classes whose names start with `Test` (and whose methods start with `test_`)

**Example:**

```python
def test_user_login():
    ...

class TestUserProfile:
    def test_update_profile(self):
        ...