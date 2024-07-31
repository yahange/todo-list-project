"""
This module provides a command-line interface for managing a to-do list.
It allows users to add, delete, list, and mark tasks as completed.
"""

import cmd
import csv

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
        with open(self.filename, 'r', encoding='utf-8') as f:
            r = csv.reader(f)
            for row in r:
                self.tasks.append([row[0], int(row[1])])

    def do_add(self, arg):
        """
        Add a new task, usage: add [task]
        """
        for task in self.tasks:
            if arg == task[0]:
                print('Task already exists.')
                return
        self.tasks.append([arg, 0])
        print(f'Task \'{arg}\' added.')

    def do_delete(self, _arg):
        """
        Delete all tasks, usage: delete
        """
        self.tasks = []
        print('All tasks have been deleted.')

    def do_list(self, _arg):
        """
        List all tasks, usage: list
        """
        if not self.tasks:
            print('No tasks available.')
            return
        for idx, task in enumerate(self.tasks, 1):
            state = 'completed' if task[1] == 1 else 'not completed'
            print(f'{idx}. {task[0]} ({state})')

    def do_save(self, _arg):
        """
        Save all tasks to a CSV file, usage: save
        """
        with open(self.filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(self.tasks)
        print('Tasks have been saved.')

    def do_complete(self, arg):
        """
        Mark a task as completed, usage: complete [task]
        """
        for task in self.tasks:
            if task[0] == arg:
                task[1] = 1
                print(f'Task \'{arg}\' marked as completed.')
                return
        print(f'Task \'{arg}\' not found.')

    def do_exit(self, _arg):
        """
        Exit the application, usage: exit
        """
        print('Exiting the To-Do List App. Goodbye!')
        return True


if __name__ == '__main__':
    ToDoCLI().cmdloop()
