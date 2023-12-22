FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-to items. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()  # It will create a list named todos
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)  # This method gets a list as the argument. In this case todos.
