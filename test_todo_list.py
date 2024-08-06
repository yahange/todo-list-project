"""
Unit tests for the ToDoCLI class in todo_list_main.py.
"""

import unittest
from todo_list_main import ToDoCLI


class TestToDoCLI(unittest.TestCase):
    """
    Test suite for the ToDoCLI class.
    """

    def setUp(self):
        """Set up a test instance of the ToDoCLI class."""
        self.cli = ToDoCLI()
        self.cli.tasks = []

    def test_add_task(self):
        """Test adding a new task."""
        self.cli.do_add("Test task")
        self.assertIn(["Test task", 0], self.cli.tasks)

    def test_add_existing_task(self):
        """Test adding a task that already exists."""
        self.cli.tasks = [["Test task", 0]]
        self.cli.do_add("Test task")
        self.assertEqual(self.cli.tasks.count(["Test task", 0]), 1)

    def test_delete_tasks(self):
        """Test deleting all tasks."""
        self.cli.tasks = [["Test task", 0]]
        self.cli.do_delete("")
        self.assertEqual(len(self.cli.tasks), 0)

    def test_list_tasks(self):
        """Test listing tasks."""
        self.cli.tasks = [["Test task", 0]]
        with self.assertLogs(level='INFO') as log:
            self.cli.do_list("")
        self.assertIn("INFO:root:1. Test task (not completed)", log.output)

    def test_complete_task(self):
        """Test marking a task as completed."""
        self.cli.tasks = [["Test task", 0]]
        self.cli.do_complete("Test task")
        self.assertIn(["Test task", 1], self.cli.tasks)

    def test_complete_nonexistent_task(self):
        """Test marking a nonexistent task as completed."""
        self.cli.do_complete("Nonexistent task")
        self.assertNotIn(["Nonexistent task", 1], self.cli.tasks)

    def test_save_tasks(self):
        """Test saving tasks to a CSV file."""
        self.cli.tasks = [["Test task", 0]]
        self.cli.save_tasks()
        with open(self.cli.filename, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn("Test task,0", content)


if __name__ == '__main__':
    unittest.main()
