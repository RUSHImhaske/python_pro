#create a list 
tasks = []

def show_task():
    print("\n--Here is your tasks--: \n")
    for task_index,task in enumerate(tasks,start=1):
        print(f"--{task_index}.{task}--")

def mark_task(num):
    print("---marking to Your Task---")
    for task_index,task in enumerate(tasks,start=0):
        if task_index == num-1:
            print(f"--task number {task_index + 1} and task is--{task}-- marked ✓ -- ")
            tasks[num-1]=task+ str("✓")
    
        else:
            pass

    


while True:
    print("welcome to TO-DO python list")
    print("press 1 : Add a task")
    print("press 2 : show task")
    print("press 3 : mark complete")
    print("press 4 : remove task")
    print("press 5 : to exit from application\n")

    choice  = int(input(" -- Select an option -- "))

    if choice == 1:
        task_name = input("please Enter Your Task \n")
        tasks.append(task_name)
        print("this is your {}".format(task_name))

    elif choice == 2:
        show_task()

    elif choice == 3:
        show_task()
        complete_task = int(input("\n --Enter the number which task is complete-- \n"))
        mark_task(complete_task)
        print("\n --Your task is updated -- \n")


    elif choice == 4:
        show_task()
        task_number = int(input("\n --please enter a task number you want to remove--\n"))
        if 1<= task_number <=len(tasks):
            remove_task = tasks.pop(task_number-1)
            print("your task is {} removed ".format(remove_task))

        else:
            print("invalid task number")

    elif choice == 5:
        print("Exiting the app")
        break
    else:
        print("\n you enter invalid number \n -----------sorry-----------\n")



        


    


    

