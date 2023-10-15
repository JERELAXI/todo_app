import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key="todo", size=45)
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.getTodos(), key='todos',
                      enable_events=True, size=[43, 5])
edit_button = sg.Button('Edit')
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.getTodos()
            new_todos = values['todo'] + '\n'
            todos.append(new_todos)
            functions.writeTodos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todos = values['todo'] + '\n'

            todos = functions.getTodos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todos
            functions.writeTodos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
