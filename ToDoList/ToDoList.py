tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print ("Current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index+1}. {task}") #+1 so list of tasks starts with 1 not 0
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: ")) - 1  #substract so it is correct value with our index
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete + 1} has been removed.") #add 1 to have correct index
        else:
            print(f"Task #{taskToDelete + 1} was not found.") #add 1 to have correct index
    except:
        print("Invalid input.")

if __name__ == "__main__":
    #Create loop for app
    print("Welcome to the to do list app")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("-------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice -> ")

        if(choice == "1"):
            addTask()
        elif(choice =="2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            break
        else:
            print("Invalid input. Try again.")
    print("Goodbye")

    #