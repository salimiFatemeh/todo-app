# حلقه بی نهایت برای لیست انجام کار

# user_prompt="Enter a todo: "
# todos=[]
# while True:
#     todo=input(user_prompt)
#     todos.append(todo)
#     print(todos)

# حلقه انجام کار با اضاف کردن و نشان دادن آن ها و پایان

# import functions
from functions import set_todos,get_todos

user_prompt = "Enter a to do: "
todos=[]

while True:
    user_action = input("Enter add,show,edit,complete or exit: ")

    # if "add" in user_action or "new" in user_action:
    if user_action.startswith("add"):

        try:

            # todo=input("Enter a to do: ")+"\n"
            todo=user_action[4:]+"\n"

            # file=open("todos.txt","r")
            # todos=file.readlines()

            # with open("todos.txt","r") as file:
            #     todos = file.readlines()

            todos=get_todos()

            todos.append(todo)

            # file=open("todos.txt","w")
            # file.writelines(todos)

            # with open("todos.txt", "w") as file:
            #     file.writelines(todos)

            set_todos(todos)

            # file.close()

        except IndexError:
            print("Your Index is out of range")

        except ValueError:
            print("You did not enter a number")

    # elif "show" in user_action:
    elif user_action.startswith("show"):

        # print(todos)1
        # چاپ اسامی به صورت لیست 1

        # for todo in todos:2
        #      print(todo)2
        # چاپ اسامی به صورت ستونی2

        # file=open("todos.txt","r")
        # todos=file.readlines()
        # file.close()

        # with open("todos.txt", "r") as file:
        #     todos=file.readlines()

        todos=get_todos()

        for index,todo in enumerate(todos):
                # پاک کردن خط خالی بین خطوط فایل
            todo=todo.strip("\n")
            print(index+1,"_",todo)
                # index با صفر شروع میشود
                # چاپ اسامی ب ترتیب و با عدد در ستون های جداگانه

    # elif "edit" in user_action:
    elif user_action.startswith("edit"):

        try:

            tods=get_todos()

            number=user_action[5:]
            # number = input("Enter a number to edit: ")
            number = int(number) - 1
            new_todo = input("Enter a todo: ")+"\n"
            todos[number] = new_todo

            # file = open("todos.txt", "w")
            # file.writelines(todos)
            # file.close()

            # with open("todos.txt", "w") as file:
            #     file.writelines(todos)

            set_todos(todos)

        except IndexError:
            print("Your Index is out of range")

    # elif "complete" in user_action:
    elif user_action.startswith("complete"):

        try:

            todos=get_todos()

            number=user_action[9:]
            # number=int(input("Enter a number to complete: "))
            number=int(number)-1
            todo_to_remove=todos[int(number)].strip("\n")
            todos.pop(number)
            print(f"Todo {todo_to_remove} has been completed!")

            # file = open("todos.txt", "w")
            # file.writelines(todos)
            # file.close()

            # with open("todos.txt", "w") as file:
            #     file.writelines(todos)

            set_todos(todos)

        except ValueError:
            print("You did not enter a number")

    # elif "exit" in user_action:
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid input")

print("Done!")