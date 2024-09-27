# To-Do List
import ToDoListFuncs as list

# Constant
STARS = 50

# Make line of stars
stars = '\n' +'*' * STARS

array = []

print('Welcome to To-Do List in Python!')

while True:
    try:
        length = len(array)
        print('What would you like to do?')
        print('\t1 - Add a task to To-Do List\n\t2 - Edit a task\n\t3 - Delete a task from To-Do List\n\t4 - Review To-Do List\n\t5 - Delete To-Do List\n\t6 - Quit')
        option = int(input('Option: '))
        print(stars)
        if option == 6:
            break
        else:
            if option == 1:
                list.add(array, length)
            elif option == 2:
                list.edit(array, length)
            elif option == 3:
                list.deleteTask(array, length)
            elif option == 4:
                if length != 0:
                    print("Here is your current To-Do List:")
                list.review(array, length)
            elif option == 5:
                list.deleteList(array, length)
            else:
                print("Please input a value of 1 - 5 matching the task you would like to perform.", stars)
    except:
        print("Please input a value of 1 - 5 matching the task you would like to perform.", stars)