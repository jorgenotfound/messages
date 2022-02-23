

def read_file(file_name):
    """
    Read a file and return its line.
    :param file_name: (str) the file's name.
    :return: (iterable) the lines extracted from the file.
    """
    f = open(file_name, "r")
    return f.readlines()
