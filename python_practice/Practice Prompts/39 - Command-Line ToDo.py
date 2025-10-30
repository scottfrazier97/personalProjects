def command_todo():

    commands = "Type A to add an item | R to remove an item | Q to quit program || Example: A: Buy milk"
    print(commands)

    todo_list = set()
    
    while True:

        if len(todo_list) == 0:
            print("\nEmpty List!\n")
        else:
            print("\nCurrent List:", [item for item in todo_list])

        user_input = input("Input Command:").strip().lower()

        if len(user_input) > 1:
            actionable_item = user_input.split(":")[1].lstrip()

        if user_input[0] == "q":
            return todo_list
        elif user_input[0] == "a" and actionable_item not in todo_list:
            todo_list.add(actionable_item)
        elif user_input[0] == "r":
            todo_list.remove(actionable_item)
        else:
            print("Invalid input")

command_todo()