FILEPATH = 'todos.txt'


def getTodos(filePath=FILEPATH):
    with open(filePath, 'r') as file:
        todos = file.readlines()
        return todos


def writeTodos(listName, filePath=FILEPATH):
    with open(filePath, 'w') as file:
        file.writelines(listName)
