from tasks import *
if __name__ == "__main__":
    menu={'P' : 'Print tasks', 
'A' : 'Add a task',
'U' : 'Update a task',
'D' : 'Delete a task',
'SI' : 'Show incomplete tasks',
'SC' : 'Show completed task',
'SP' : 'Show tasks sorted by priority, highest first',
'SD' : 'Show tasks sorted by due date, earliest first',
'S' : 'Save tasks',
'L' : 'Load tasks from file',
'Q' : 'Quit this program'}
    task_list=[]
    while True:
        print_main_menu(menu)
        print("::: Enter an option")
        opt=input("> ")
        if opt=='Q':
            print("See you next time!")
            break
        else:
            while  check_option(opt, menu)=="invalid":
                print('::: Enter a valid option')
                opt=input("> ")
            print(f"You selected option {opt} to > {menu[opt]}")
            if opt=='P':
                print_formatted_tasks(task_list) 
            elif opt=='A':
                name=input('name: ')
                description=input('description: ')
                date=input('date: ')
                priority=input('priority: ')
                completed=input('completed: ')
                if create_a_task(name, description, date, priority, completed)[0]:
                    task_list.append(create_a_task(name, description, date, priority, completed)[1])
                else:
                    print('Invalid data: '+create_a_task(name, description, date, priority, completed)[1])
            elif opt=='U':
                task_id=input('task_id: ')
                task_field=input('task_field: ')
                task_update=input('task_update: ')
                update_task(task_list,task_id,task_field,task_update)
            elif opt=='D':
                task_id=input('task_id: ')
                delete_task(task_id,task_list)
            elif opt=='SI':
                print_tasks_by_status(task_list, False)
            elif opt=='Sc':
                print_tasks_by_status(task_list, True)
            elif opt=='SP':
                print_sorted_priority(task_list)
            elif opt=='SD':
                print_sorted_deadline(task_list)
            elif opt=='S':
                filename=input('filename: ')
                save_to_csv(task_list,filename)
            elif opt=='L':
                filename=input('filename: ')
                load_from_csv(filename)
            elif opt=='Q':
                break
            else:
                print('This option is not yet implemented')
            opt=input("::: Press Enter to continue...")
    print("Have a productive day!")
