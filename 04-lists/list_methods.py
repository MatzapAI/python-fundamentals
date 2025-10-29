print("---TASK LIST---")

tasks = ["clean", "study", "buy food"]

while True:
    print("\nPENDING TASKS")
    print(tasks)

    print("Options. \n1.Add task \n2.Urgent task \n3.Complete task \n4.Close program")
    option = input("Enter one option: ")

    if not option.isdigit():
       print("Invalid input... Try again")
       continue 

    option = int(option)

    if option == 1:
        add_task = input("What task do you want to enter?: ").lower()
        tasks.append(add_task)
    elif option == 2:
        add_task = input("What is the important task?: ").lower()
        tasks.insert(0, add_task)
    elif option == 3:
        print(tasks)
        remove_task = input("What task have you completed?: ").lower()
        tasks.remove(remove_task)
        print("Task complete 👌")
    elif option == 4:
        print("Closing the program...")
        break
    else:
        print("Invalid option.Try again")


