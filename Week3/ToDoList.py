# To-Do List

STARS = 50
stars = '\n' +'*' * STARS

list = []

print('Welcome to To-Do List in Python!')

def add(length):
    task = input("What is your task to add? ")
    list.append(task.strip())
    print("Your task has been added to your To-Do List.")
    length = len(list)
    review(length)


def edit(length):
    if length == 0:
        print("There are currently no tasks in your To-Do List to edit.", stars)
    else:
        while True:
            try:
                print("Here is your current To-Do List:")
                countList(length)
                task = int(input("Which task would you like to edit (Enter '0' to quit)? ")) - 1
                if task in range(length):
                    new_task = input("What would you like your new task to be? ").strip()
                    list[task] = new_task
                    print("Your task has been updated. Here is your new To-Do List:")
                    review(length)
                    break
                elif task == -1:
                    break
                else:
                    print("You inputted a value that is not an option.", stars) 
            except:
                print("You inputted a value that is not an option.", stars) 


def deleteTask(length):
    if length == 0:
        print("There are currently no tasks in your To-Do List to delete.", stars)
    else:
        while True:
            try:
                print("Here is your current To-Do List:")
                countList(length)
                task = int(input("Which task would you like to remove (Enter '0' to quit)? ")) - 1
                if task in range(length):
                    list.remove(list[task])
                    print("Task successfully removed. Here is your new To-Do List:")
                    review(length)
                    break
                elif task == -1:
                    break
                else:
                    print("That is not an option in your current To-Do List.", stars)
            except:
                print("You did not input an integer value so editing was aborted.", stars) 



def review(length):
    if length == 0:
        print("Unable to review your To-Do List because it is currently empty.", stars)
    else:
        for item in list:
            print(f'\t- {item}')
        print(stars)


def deleteList(length):
    if length == 0:
        print("Unable to delete your To-Do List because it is currently empty.", stars)
    else:
        while True:
            sure = input("Are you sure you want to delete your entire To-Do List? (y/n) ").lower()
            if sure[0] == 'y':
                list.clear()
                print("Your To-Do List has been deleted.", stars)
                break
            elif sure[0] == 'n':
                break
            else:
                print("Please input 'y' for Yes or 'n' for No as your answer.", stars)


def countList(length):
    for i in range(length):
            print('\t{}. {}'.format((i + 1), list[i]))


while True:
    try:
        length = len(list)
        print('What would you like to do?')
        print('\t1 - Add a task to To-Do List\n\t2 - Edit a task\n\t3 - Delete a task from To-Do List\n\t4 - Review To-Do List\n\t5 - Delete To-Do List\n\t6 - Quit')
        option = int(input('Option: '))
        print(stars)
        if option == 6:
            break
        else:
            if option == 1:
                add(length)
            elif option == 2:
                edit(length)
            elif option == 3:
                deleteTask(length)
            elif option == 4:
                if length != 0:
                    print("Here is your current To-Do List:")
                review(length)
            elif option == 5:
                deleteList(length)
            else:
                print("Please input a value of 1 - 5 matching the task you would like to perform.", stars)
    except:
        print("Please input a value of 1 - 5 matching the task you would like to perform.", stars)