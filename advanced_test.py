def create_squares_of_evens():
    """
    Task:
    - Create a list of squares for all even numbers from 1 to 20 using list comprehension.
    
    Return:
    - The list of squares of even numbers.
    """
    list_1 = [x**2 for x in range(1,11) if x % 2 == 0 ]
    return list_1

def convert_to_dict(students):
    """
    Task:
    - Convert the list of student tuples into a dictionary where the name is the key and the grade is the value.
    
    Return:
    - The dictionary created from the list of students.
    """
    dict_1 = {}

    for student in students:
        dict_1.update({student[0]:student[1]})
    return dict_1

print(convert_to_dict([('Alice', 85), ('Bob', 90), ('Charlie', 78), ('David', 92)]))
    

def access_value_x(nested):
    """
    Task:
    - Access the value of 'x' from the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The value of 'x' (which is 10).
    """
    for k,v in nested.items():
        if k == 'c':
            for k_1,v_1 in v.items():
                if k_1 == 'x':
                    return v_1


def append_to_list_in_dict(nested):
    """
    Task:
    - Append the value 6 to the list under key 'a' in the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The updated dictionary.
    """
    for k,v in nested.items():
        if k == 'a':
            v.append(6)
    return nested



def convert_tuple_to_list_and_append(nested):
    """
    Task:
    - Convert the tuple under key 'b' in the nested dictionary into a list and add the value 6 at the end.
    
    Return:
    - The updated dictionary.
    """
    nested['b'] = [nested['b'][0],nested['b'][1]]
    nested['b'].append(6)

    return nested
