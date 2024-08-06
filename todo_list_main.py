"""
This module provides a command-line interface for managing a to-do list.
It allows users to add, delete, list, and mark tasks as completed.
"""

import cmd
import csv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class ToDoCLI(cmd.Cmd):
    """
    ToDoCLI provides a command-line interface for managing to-do tasks.
    Users can add, delete, list tasks, and mark tasks as completed.
    """
    intro = 'Welcome to the To-Do List App. Type help or ? to list commands.\n'
    prompt = '(todo) '

    def __init__(self):
        super().__init__()
        self.filename = 'todo_list.csv'
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the CSV file."""
        if not os.path.exists(self.filename):
            logging.info("File %s not found. Starting with an empty task list.", self.filename)
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                r = csv.reader(f)
                for row in r:
                    self.tasks.append([row[0], int(row[1])])
        except OSError as e:
            logging.error("Error reading %s: %s", self.filename, e)

    def save_tasks(self):
        """Save tasks to the CSV file."""
        try:
            with open(self.filename, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(self.tasks)
            logging.info('Tasks have been saved.')
        except OSError as e:
            logging.error("Error saving to %s: %s", self.filename, e)

    def do_add(self, arg):
        """
        Add a new task, usage: add [task]
        """
        if not arg:
            logging.warning("Task description cannot be empty.")
            return

        for task in self.tasks:
            if arg == task[0]:
                logging.warning('Task already exists.')
                return
        self.tasks.append([arg, 0])
        logging.info("Task '%s' added.", arg)

    def do_delete(self, _arg):
        """
        Delete all tasks, usage: delete
        """
        if input("Are you sure you want to delete all tasks? (y/n) ").lower() == 'y':
            self.tasks = []
            logging.info('All tasks have been deleted.')

    def do_list(self, _arg):
        """
        List all tasks, usage: list
        """
        if not self.tasks:
            logging.info('No tasks available.')
            return
        for idx, task in enumerate(self.tasks, 1):
            state = 'completed' if task[1] == 1 else 'not completed'
            logging.info('%d. %s (%s)', idx, task[0], state)

    def do_save(self, _arg):
        """
        Save all tasks to a CSV file, usage: save
        """
        self.save_tasks()

    def do_complete(self, arg):
        """
        Mark a task as completed, usage: complete [task]
        """
        for task in self.tasks:
            if task[0] == arg:
                task[1] = 1
                logging.info("Task '%s' marked as completed.", arg)
                return
        logging.warning("Task '%s' not found.", arg)

    def do_exit(self, _arg):
        """
        Exit the application, usage: exit
        """
        logging.info('Exiting the To-Do List App. Goodbye!')
        return True


if __name__ == '__main__':
    ToDoCLI().cmdloop()
