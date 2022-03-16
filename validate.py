def check_option(option, the_menu):
    """
    Check the option is valid or not
    """
    if type(option) == str and option in the_menu:
        return "valid"
    else:
        return "invalid"
        
def is_numeric(val):
    """
    Returns True if the string `val`
    contains a valid integer or a float.
    Returns False otherwise.
    """
    if type(val)==int:
        return True
    elif val.isdigit():
        return True
    elif val.count('.') == 1:
        new_value = val.split('.')
        if new_value[0].isdigit() and new_value[1].isdigit():
            return True
    return False

def is_valid_index(idx, in_list):
    """
    Checks whether the provided index `idx`
    is a valid positive index that can retrieve
    an element from `in_list`.
    Returns False if `idx` is negative or exceeds
    the size of `in_list` - 1.
    """
    if idx < 0 or idx > (len(in_list) - 1):
        return False
    else:
        return True
def validate_name(name):
    '''
    validates the "name" parameter
    Returns True if the name is between 3 and 15 characters long, inclusive
    Returns False otherwise
    '''
    if len(name)>=3 and len(name)<=15:
        return True
    else:
        return False
def validate_description(desc):
    '''
    validates the "desc" parameter
    Returns True if desc is a non-empty string
    Returns False otherwise
    '''
    if len(desc)>0:
        return True
    else:
        return False
def validate_date(date_string):
    """
    Check the date is valid or not
    """
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if date_string.count('/') == 2:
        date_list = date_string.split('/')
        for i in date_list:
            if not i.isdigit():
                return False
        month = int(date_list[0])
        day = int(date_list[1])
        year = int(date_list[2])
        if month < 1 or month > 12:
            return False
        if day < 1 or day > num_days[month]:
            return False
        return True
    else:
        return False
def validate_priority(priority):
    '''
    validate the "priority" parameter
    Returns True if "priority" is a string containing a number 1-5
    Returns False otherwise
    '''
    if priority.isdigit() == True:
        if 1 <= int(priority) <= 5:
            return True
        else:
            return False
    else:
        return False
def validate_completed(comp):
    '''
    validate the "comp" parameter.
    Returns True if s is one of: "yes", "no", "Yes", "No"
    Returns False otherwise
    '''
    if comp=='yes' or comp == 'no' or comp=='Yes' or comp=='No':
        return True
    else:
        return False
