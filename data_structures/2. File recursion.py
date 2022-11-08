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
    file_list = os.listdir(path)
    all_files = list()
    
    for entry in file_list:
        # Create full path
        full_path = os.path.join(path, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + find_files(suffix, full_path)
        else:
            if full_path.endswith(suffix):
                all_files.append(full_path)

    return all_files

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
path = r"C:\Users\32470\Desktop\coding_practice\dsa_python\data_structures\testdir"
suffix = ".c"
print(find_files(suffix, path))
# Test Case 2

# Test Case 3