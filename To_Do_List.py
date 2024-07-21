def task():
    tasks=[]
    print("<-----WELCOME TO THE TASK MANAGEMENT APPLICATION------>")

    no_task=int(input("Enter how many task you want to add: "))

    for i in range(1,no_task+1):
        add_task=input(f"Enter task {i}: ")
        tasks.append(add_task)

    print("Today's tasks are: ",tasks)

    while True:
        operation=int(input("Enter\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n--->"))
        if operation==1:
            new_task=input("Enter the new task you want to add: ")
            tasks.append(new_task)
            print(f"Task {new_task} has been successfully added....")
        elif operation==2:
            update_task=input("Enter the task name you want to update: ")
            if update_task in tasks:
                new_update=input("Enter the new task: ")
                indx=tasks.index(update_task)
                tasks[indx]=new_update
                print(f"Task {new_update} has been successfully updated....")
            else:
                print("Invalid task!")
        elif operation==3:
            delete_task=input("Enter task name you want to delete: ")
            if delete_task in tasks:
                tasks.remove(delete_task)
                print(f"Task {delete_task} has been successfully deleted....")
            else:
                print("Invalid task!")
        elif operation==4:
            print(f"Total tasks: {tasks}")
        elif operation==5:
            print("Closing the program....")
            break
        else:
            print("Invalid Input!")        

task()