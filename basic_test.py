def int_division():
    """
    Task:
    - Perform integer division of 7 by 2.
    
    Return:
    - The result of the division (integer).
    """
    results = 7 // 2
    return results


def float_multiplication():
    """
    Task:
    - Multiply 3.0 by 2.
    
    Return:
    - The result of the multiplication (float).
    """
    results = 3.0 * 2
    return results


def combine_operations():
    """
    Task:
    - Add the result of integer division and multiplication.
    
    Return:
    - The combined result (float).
    """
    result = int_division() + float_multiplication() - 3
    return result

print(combine_operations())


def extract_word():
    """
    Task:
    - Extract the word 'awesome' from the string 'Python is awesome!'.
    
    Return:
    - The extracted word ('awesome').
    """
    string = 'Python is awesome!'
    extracted = ''

    if 'awesome' in string:
        extracted = extracted + 'awesome'
    
    return extracted

print(extract_word())


def to_lowercase():
    """
    Task:
    - Convert the string 'Python is awesome!' to lowercase.
    
    Return:
    - The lowercase version of the string.
    """
    string = 'Python is awesome!'
    return string.lower()


def count_o():
    """
    Task:
    - Count how many times the letter 'o' appears in the string 'Python is awesome!'.
    
    Return:
    - The count of the letter 'o'.
    """
    count = 0
    string = 'Python is awesome!'

    for x in string:
        if x.lower() == 'o':
            count += 1
    return count


def evaluate_boolean():
    """
    Task:
    - Evaluate the expression 'not (5 > 3) and (10 == 5 * 2)'.
    
    Return:
    - The boolean result of the expression.
    """
    result = not (5 > 3) and (10 == 5 * 2)
    return result
print(evaluate_boolean())
