# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y - %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"  # To extract everything after add...
        # (without the space between add and the next word)

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip()  # Remove \n from each string in the list
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            removed_todo = todos.pop(number - 1).strip()

            functions.write_todos(todos)

            message = f"Todo {removed_todo} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye!")
