tasks  = [] #empty list

def task_mangement ():

 print(" welcome to the task mangement ")

total_task = int(input("enter how many task you want to add =")) #5
for i in  range( 1, total_task + 1) :
      task_name=input(f"enter the task {i}=")
      tasks.append(task_name)
print(f"today task's are :\n{tasks}")

task_mangement()

while True :
    operation= int(input("enter 1-add\n2-update\n3-delete\n4-view\n5-exit/stop"))
    if operation ==1:
        add=input("enter your task ")
        tasks.append(add)
        print(f"task{add} has been successfully added ...")
    elif operation ==2:
        upadte_val=input("enter the task name you want to upadte = ")
        if upadte_val in tasks: 
         up= input ("enter your new task")
        ind =tasks.index(upadte_val) 
        tasks[ind]=up
        print(f"upadte task {up}")

    elif operation ==3:
        del_val=input("enter the taks you want to delete = ")
        if del_val in tasks:
            ind =tasks.index(del_val)
            del tasks[ind]
            print(f"task{del_val} has been deleted ")
    elif operation ==4:
        print(f"total_task ={tasks}")
    elif operation ==5:
        print("cloasing the programmm....")
        