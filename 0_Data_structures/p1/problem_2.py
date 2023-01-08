import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    if len(suffix) == 0 or len(path) == 0 or suffix == '' or path == '':
        return "Suffix not present or path is not given"
    
    if len(suffix) > len(path):
        return "Check suffix length"
    # List out all the files and directories in the given path
    file_list = os.listdir(path)
    
    # Initialize a list to store the results
    all_files = list()
    
    for entry in file_list:
        # For each sub-folder, create a full path
        full_path = os.path.join(path, entry)
        # For each sub-folder within the folder, recursively, retrive of files in each sub-folder
        if os.path.isdir(full_path):
            all_files = all_files + find_files(suffix, full_path)
        if full_path.endswith(suffix):
                all_files.append(full_path)

    return all_files

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
path = r"C:\Users\32470\Desktop\testdir"
suffix = ".c"
print(find_files(suffix, path))
# Test Case 2
path = r"C:\Users\32470\Desktop\testdir"
suffix = ""
print(find_files(suffix, path))
# Test Case 3
path = r"C:\Users\32470\Desktop\testdir"
suffix = ".caaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(find_files(suffix, path))