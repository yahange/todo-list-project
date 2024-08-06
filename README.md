# To-Do List App

This is a simple command-line based To-Do List application written in Python. The app allows users to manage their tasks efficiently. Users can add, delete, list, mark tasks as completed, and save the tasks to a CSV file. The app is designed to help users keep track of their tasks and organize their daily activities.

## Features
- **Add Tasks**: Add new tasks to your list.
- **Delete Tasks**: Remove all tasks from the list.
- **List Tasks**: Display all tasks along with their status (completed or not completed).
- **Mark as Completed**: Mark specific tasks as completed.
- **Save to CSV**: Save all tasks to a CSV file for future reference.

## Usage
1. **Add a Task**: Use the `add [task]` command to add a new task.
2. **Delete Tasks**: Use the `delete` command to remove all tasks.
3. **List Tasks**: Use the `list` command to display all tasks.
4. **Mark as Completed**: Use the `complete [task]` command to mark a task as completed.
5. **Save Tasks**: Use the `save` command to save all tasks to a CSV file.
6. **Exit**: Use the `exit` command to exit the application.

## Error Handling
- The application now includes specific error handling for file operations.
- Errors during file read and write operations are logged with appropriate error messages.

## Development and Testing
- The code includes detailed module and class docstrings.
- Logging has been updated to use lazy % formatting for better performance.
- Unit tests are provided to ensure the correctness of the main functionalities.

### Running the Application
To run the application, navigate to the project directory and execute the following command:

```bash
python todo_list_main.py
```
## Running Tests
To run the unit tests, execute the following command:
```bash
python -m unittest test_todo_list.py
```
This application is a useful tool for anyone looking to organize their tasks and increase productivity.
