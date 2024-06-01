import os

FILE_PATH = "files/todos.txt"

if not os.path.exists('files'):
    os.makedirs('files')

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'w') as file:
        pass


def get_todos(file_path=FILE_PATH):
    with open(file_path, 'r') as file:
        todos = file.readlines()
    return todos


def set_todos(todos, file_path=FILE_PATH):
    with open(file_path, 'w') as file:
        file.writelines(todos)
