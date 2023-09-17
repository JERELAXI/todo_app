from functions import getTodos, writeTodos
import time

now = time.strftime("%b, %d, %Y %H:%M:%S")
print('It is', now)

while True:
    userAction = input("Type add, show, edit, complete or exit: ").strip()

    if userAction.startswith('add'):
        todo = userAction.strip('add ')  # userAction[4:]

        todos = getTodos()

        todos.append(todo.capitalize() + '\n')

        writeTodos(todos)
    elif userAction.startswith('show'):
        todos = getTodos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1}. {item}')
    elif userAction.startswith('edit'):
        try:
            i = int(userAction.strip('edit '))  # userAction[5:]

            todos = getTodos()

            todo = input("Enter new todo: ")
            todos[i - 1] = todo + '\n'

            writeTodos(todos)
        except ValueError:
            print('Your command is not valid.')
            continue

    elif userAction.startswith('complete'):
        try:
            i = int(userAction.strip('complete '))  # userAction[9:]

            todos = getTodos()

            removed = todos.pop(i - 1).strip('\n')

            writeTodos(todos)

        except IndexError:
            print('There is no item with that number.')
            continue

        print(f'Todo {removed} was removed from the list.')
    elif userAction.startswith('exit'):
        print('Bye!')
        break
    else:
        print("Hey, you entered an unknown command!")
