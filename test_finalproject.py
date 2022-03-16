from tasks import * 

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


my_list=[{'name':'asdasd','description':'dasdasdasd',
    'deadline':'02/02/2021','priority':3,'completed':'yes'}]

my_list2=[{'name':'asdasd','description':'dasdasdasd',
    'deadline':'02/02/2021','priority':3,'completed':'no'}]

assert check_option('P', menu) =='valid'

assert check_option('s', menu) =='invalid'

assert create_a_task('asdasd', 'dasdasdasd', '02/02/2021', '3', 'yes')==(True,{
    'name':'asdasd','description':'dasdasdasd',
    'deadline':'02/02/2021','priority':3,'completed':True})

assert create_a_task('asdasd', 'dasdasdasd', '02/02/2021', '9', 'yes')==(False,'priority')

assert create_a_task('asdasd', 'dasdasdasd', '02/02/2021', '3', 'asd')==(False,'completed')

assert slashes_to_written(['02','02','2022'])=='February 2, 2022'

assert print_tasks_by_status(my_list, False)=='You do not have incomplete tasks.'

assert print_tasks_by_status(my_list2, True)=='You do not have completed tasks.'

assert update_task(my_list,0,'name','as')==(False, 'Name caused the error during validation')

assert update_task(my_list,0,'name','asdasdsa')==(True,my_list[0])

assert delete_task(1,my_list)== False

assert delete_task(0,my_list)== True