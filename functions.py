"""
Functions and classes used for the Micron browser.
"""

def recreate_string(variable:(list, tuple), char_in_between:str=""):
    """
    Recreates a string from a list.
    Parameter 'variable' (list) : The list to put together to a string.
    Parameter 'char_in_between' (str) : The char to put between the elements to recompose. Nothing by default.
    """
    temp_str = ""
    for element in variable:
        temp_str += str(element) + char_in_between
    return temp_str

