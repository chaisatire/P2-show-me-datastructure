import os


def find_files(suffix, path):
    """
        Parent function which calls recursive function.
        We first check for if directory exists and if it does exist we create
        an empty list to store the file names.
    """
    if not os.path.isdir(path):
        return "Directory Not found, please provide a correct directory"
    list_files = list()
    return _find_files_function(suffix, path, list_files)


def _find_files_function(suffix, path, list_files):
    """
        Recursive function which checks for the directory and file suffix.
        If it find a directory it checks it recursively. In the end append
        the file name to list_files if the file with correct suffix is found.
    """
    for files in os.listdir(path):
        updated_file_path = path + '/' + files
        if os.path.isdir(updated_file_path):
            _find_files_function(suffix, updated_file_path, list_files)
        else:
            if updated_file_path.endswith('.c'):
                list_files.append(files)
    return list_files


## Test Case 1
print(find_files('.c', 'testdir'))

## Test Case 2
print(find_files('.a', 'empty'))

## Test Case 3
print(find_files('.a', 'testdir'))
