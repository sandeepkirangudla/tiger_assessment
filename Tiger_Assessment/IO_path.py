import os


def output_path(path):
    """
    This function takes input path and checks if file exist.
    """
    a = True
    while a == True:
        path = input(path)
        if os.path.isdir(path):
            a = False
            return path
        else:
            print('Please enter a valid input path')
