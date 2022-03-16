from validate import *

import csv


def print_main_menu(menu):
    """
    Given a dictionary `menu`,
    prints the keys and values as the
    formatted options of a menu.
    Adds additional prints for decoration
    and to output a question
    "What would you like to do?"
    """
    print("**************************")
    print('What would you like to do?')
    for key, value in menu.items():
        print(key, '-', value)
    print("**************************")
def check_option(opt, menu):
    """
    Given an option, return "valid" if it is
    of type str and is a valid key in
    the provided `menu` collection.
    Otherwise, return "invalid".
    """
    if type(opt) == str and opt in menu:
        return "valid"
    return "invalid"

def create_a_task(name, description, date, priority, completed):
    '''
    validate each parameter starting from "name" and until "completed"
    If one of them fails, return (False, <name of parameter>)
    ex. (False, "name") if "name" is not 3-15 characters long
    or (False, "completed") if completed is not a "yes" or "no"
    If all validations pass, return (True, <dictionary with fields name, description...>)
    '''
    if validate_name(name) != True:
        return (False, 'name')
    elif validate_description(description) != True:
        return (False, 'description')
    elif validate_date(date) != True:
        return (False, 'deadline')
    elif validate_priority(priority) != True:
        return (False, 'priority')
    elif validate_completed(completed) != True:
        return (False, 'completed')
    else:
        if completed == 'yes' or completed == 'Yes' or completed == 'True':
            completed = True
        else:
            completed = False
        get = {
            'name': name,
            'description': description,
            'deadline': date,
            'priority': int(priority),
            'completed': completed
        
        }
        
        return (True,get)
        

def slashes_to_written(date_list):
    """
    Change list of dates in to the date form that
    we want
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    # Finish the function
    month = month_names[int(date_list[0])]
    day = str(int(date_list[1]))
    result = f'{month} {day}, {date_list[2]}'
    return result

def formatted_completed(completed):
    """
    change the completed status from boolean to Yes or No
    """
    if completed==True:
        return 'Yes'
    else:
        return 'No'

def boolean_completed(completed):
    """
    change the completed status from Yes or No to Boolean
    """
    if completed=='yes' or completed=='Yes' or completed=='True' or  completed==True:
        return True
    else:
        return False

def formatted_priority(priority):
    """
    Change the priority into status(str)
    """
    if priority==1:
        return 'Lowest'
    elif priority==2:
        return 'Low'
    elif priority==3:
        return 'Medium'
    elif priority==4:
        return 'High'
    else:
        return 'Highest'


def print_formatted_tasks(tasks_list):
    """
    print_formatted_tasks, each attributes on by one
    """
    index = 0
    for i in tasks_list:
        print(f"{index}:  {i['name'].upper()}")
        print(f"    Description: {i['description']}")
        print(f"    Priority: {formatted_priority(i['priority'])}")
        print(f"    Deadline: {slashes_to_written(i['deadline'].split('/'))}")
        print(f"    Completed: {formatted_completed(i['completed'])}")
        index += 1
        print()
def print_tasks_by_status(all_tasks, completed=False):
    """ Prints tasks from 'all_tasks', based on the value of 'completed' of each task. 
    If there are no tasks that are incomplete, prints 'You do not have incomplete tasks.'
    If there are no tasks that are completed, prints 'You do not have completed tasks.' 
    Otherwise, prints the requested tasks. """
    c=0
    inc=0
    tasks_listT=[]
    tasks_listF=[]
    if len(all_tasks)==0:
        return None
    for i in all_tasks:
        if i['completed'] in ['Yes','yes']:
            c+=1
            tasks_listT.append(i)
        elif i['completed'] in ['No','no']:
            inc+=1
            tasks_listF.append(i)
    if completed==False and c==len(all_tasks):
        print('You do not have incomplete tasks.')
    elif completed==True and inc==len(all_tasks):
        print('You do not have completed tasks.')
    else:
        if completed==False:
            print_formatted_tasks(tasks_listF)
        else:
            print_formatted_tasks(tasks_listT)
        

def update_task(task_list,task_id,task_field,task_update):
    """ 
    Update one of the task in the task lists depending on the task field
    if the inputs are valid, we update the content of the task
    """
    fields=[
        'name',
        'description',
        'deadline',
        'priority',
        'completed'
    ]
    if not (is_numeric(task_id) and is_valid_index(task_id, task_list)):
        return (False,'idx')
    
    if check_option(task_field, fields)=='invalid':
        return (False,'field')
    
    if task_field=='name':
        if validate_name(task_update):
            task_list[task_id]['name']=task_update
            return (True,task_list[task_id])
        else:
            return (False,'name')
    elif task_field=='description':
        if validate_description(task_update):
            task_list[task_id]['description']=task_update
            return (True,task_list[task_id])
        else:
            return (False,'description')
    elif task_field=='deadline':
        if validate_date(task_update):
            task_list[task_id]['deadline']=task_update
            return (True,task_list[task_id])
        else:
            return (False,'deadline')    
    elif task_field=='priority':
        if validate_priority(task_update):
            task_list[task_id]['priority']=task_update
            return (True,task_list[task_id])
        else:
            return (False,'priority')    
    elif task_field=='completed':
        if validate_completed(task_update):
            task_list[task_id]['completed']=boolean_completed(task_update)
            return (True,task_list[task_id])
        else:
            return (False,'completed')    

def print_sorted_priority(all_tasks):
    """ 
    Print all tasks based on the priority
    Highest priority will be first
    """
    newlist = sorted(all_tasks, key=lambda d: d['priority'],reverse=True)
    print_formatted_tasks(newlist)

def compare_time(date):
    """ 
    Change the data into number and can be compared with each other
    e.g: '02/02/2021' to 20210202
    so that we can use it in  print_sorted_deadline
    """
    date=date.split('/')
    num_date=int(date[2]+date[1]+date[0])
    return num_date


def print_sorted_deadline(all_tasks):
    """ 
    Print all tasks based on the deadline
    Closest deadline will be first
    """
    newlist = sorted(all_tasks, key=lambda d: compare_time(d['deadline']))
    print_formatted_tasks(newlist)

def delete_task(idx,tasks):
    """ 
    delete a task based on the index
    """
    if is_valid_index(idx,tasks):
        tasks.pop(idx)
        return True
    else:
        return False

def save_to_csv(my_list,filename):
    """ 
    save the list into csv file following the rule 
    """
    with open(filename,'w',newline='') as myfile:
        task_writer=csv.writer(myfile)
        for i in my_list:
            task_data=list(i.values())
            task_writer.writerow(task_data)


def load_from_csv(filename):
    """ 
    read the csv file and transform it into list following our rule
    """
    my_list=[]
    with open(filename,'r',newline='') as myfile:
        reader_object=csv.reader(myfile)
        for values in reader_object:
            if len(values)==5:
                if values[4]=='True':
                    values[4]='yes'
                else:
                    values[4]='no'
                result=create_a_task(values[0],values[1],values[2],values[3],values[4])
                if result[0]:
                    my_list.append(result[1])
                else:
                    return "invalid data"
            else:
                return "inconsistent format"
        return my_list
