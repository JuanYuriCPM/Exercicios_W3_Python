"""
50. Write a Python program to print without a newline or space
"""

def no_new_line_or_space(string):
    """
    Removes all whitespaces and newlines from a string

    Args:
    string: the string analyzed
    Returns: 
    The analyzed string after removing all instances of whitespace and new line from it.
    """
    new_list = string.split()
    new_string = ''
    for i in new_list:
        new_string += i
    return new_string

print(no_new_line_or_space('New\ntesting\nsentence     for\n   \n   python'))