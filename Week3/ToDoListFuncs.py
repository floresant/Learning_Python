# Constant
STARS = 50

# Make line of stars
stars = '\n' +'*' * STARS

def add(arr, length):
    """This function adds a task to the To-Do List"""
    task = input("What is your task to add? ")
    arr.append(task.strip())
    print("Your task has been added to your To-Do List.")
    length = len(arr)
    review(arr, length)


def edit(arr, length):
    """This function edits a task in the To-Do List"""
    if length == 0:
        print("There are currently no tasks in your To-Do List to edit.", stars)
    else:
        while True:
            try:
                print("Here is your current To-Do List:")
                countList(arr, length)
                task = int(input("Which task would you like to edit (Enter '0' to quit)? ")) - 1
                if task in range(length):
                    new_task = input("What would you like your new task to be? ").strip()
                    arr[task] = new_task
                    print("Your task has been updated. Here is your new To-Do List:")
                    review(arr, length)
                    break
                elif task == -1:
                    break
                else:
                    print("You inputted a value that is not an option.", stars) 
            except:
                print("You inputted a value that is not an option.", stars) 


def deleteTask(arr, length):
    """This function deletes a task in the To-Do List"""
    if length == 0:
        print("There are currently no tasks in your To-Do List to delete.", stars)
    else:
        while True:
            try:
                print("Here is your current To-Do List:")
                countList(arr, length)
                task = int(input("Which task would you like to remove (Enter '0' to quit)? ")) - 1
                if task in range(length):
                    arr.remove(arr[task])
                    print("Task successfully removed. Here is your new To-Do List:")
                    review(arr, length)
                    break
                elif task == -1:
                    break
                else:
                    print("That is not an option in your current To-Do List.", stars)
            except:
                print("You did not input an integer value so editing was aborted.", stars) 



def review(arr, length):
    """This function prints every item in the To-List List on a tabbed new line with '-'"""
    if length == 0:
        print("Unable to review your To-Do List because it is currently empty.", stars)
    else:
        for item in arr:
            print(f'\t- {item}')
        print(stars)


def deleteList(arr, length):
    """This function deletes the entire To-Do List"""
    if length == 0:
        print("Unable to delete your To-Do List because it is currently empty.", stars)
    else:
        while True:
            sure = input("Are you sure you want to delete your entire To-Do List? (y/n) ").lower()
            if sure[0] == 'y':
                arr.clear()
                print("Your To-Do List has been deleted.", stars)
                break
            elif sure[0] == 'n':
                break
            else:
                print("Please input 'y' for Yes or 'n' for No as your answer.", stars)


def countList(arr, length):
    """This function prints every item in the To-List List on a tabbed new line with an incrementing integer"""
    for i in range(length):
            print('\t{}. {}'.format((i + 1), arr[i]))
