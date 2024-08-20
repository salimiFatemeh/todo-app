def get_todos():
    # برای توضیحات
    """
    please use this function whenever
    you wanna have todos list
    :return: todos list
    """
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return todos

def set_todos(todos):
    """
    please use this function when you want
    to take input and ensert it in the list
    :param todos: list of todos
    """
    with open("todos.txt", "w") as file:
        file.writelines(todos)