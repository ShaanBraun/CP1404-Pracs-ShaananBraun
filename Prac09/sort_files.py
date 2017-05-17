import os, shutil

ROOT_DIRECTORY = "FilesToSort"


def main():
    # Testing Code
    # test_list = ["Docs", "jpg"]
    # make_sorted_directories(ROOT_DIRECTORY, test_list)
    # print(parse_filetype("hello.txt"))
    #
    # Test User Sorting and Parsing in One
    # file_list_types = []
    # for filename in os.listdir(ROOT_DIRECTORY):
    #
    #     if not os.path.isdir(os.path.join(ROOT_DIRECTORY, filename)):
    #         if parse_filetype(filename) not in file_list_types:
    #             file_list_types.append(parse_filetype(filename))
    #
    # print(file_list_types)
    # print(get_user_sorting_choice(file_list_types))
    #
    # Test Making Directories from file user choice from file extensions.
    # user_choice, directories = get_user_sorting_choice(parse_file_type(load_filenames(ROOT_DIRECTORY)))
    # make_sorted_directories(ROOT_DIRECTORY, directories)
    # sort_filetypes_to_directory(user_choice, ROOT_DIRECTORY)

    user_filetype_to_dir_assocation, user_sorting_directories = get_user_sorting_choice(
        parse_file_type(load_filenames(ROOT_DIRECTORY)))

    make_sorted_directories(ROOT_DIRECTORY, user_sorting_directories)

    sort_filetypes_to_directory(user_filetype_to_dir_assocation, ROOT_DIRECTORY)


def sort_filetypes_to_directory(filetype_assocation, directory):
    for filename in os.listdir(directory):
        current_file_path = os.path.join(directory, filename)
        if not os.path.isdir(current_file_path):
            destination_path = os.path.join(directory, filetype_assocation[parse_file_type(filename)])
            shutil.copy(current_file_path, destination_path)


def load_filenames(directory):
    """
    Returns list of only files from specified directory.

    :return:
    """

    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)

    return files


def parse_file_type(filenames):
    """
    Returns filetype extension(s) as a string or list or strings.

    :param filenames: String or List - Filename(s) to parse.
    :return:
    """

    if isinstance(filenames, list):
        parsed_list_of_types = []
        for file in filenames:
            try:
                file_type = file.split('.')[1]
            except IndexError:
                print(
                    "Invalid filename parsed, no filetype extension found. Expected '.something' instead got: {}".format(
                        file))
            if file_type not in parsed_list_of_types:
                parsed_list_of_types.append(file_type)
        return parsed_list_of_types
    else:
        try:
            return filenames.split('.')[1]
        except IndexError:
            print("Invalid filename parsed, no filetype extension found. Expected '.something' instead got: {}".format(
                filenames))


def get_user_sorting_choice(file_types):
    """
    Returns dictionary (with relation to filetype given) and list of strings with user choice for each of the passed in files, based on filetype.

    :param file_types: list of filetypes to ask user for sorting choice.
    :return: Dictionary of type to sorted folder. List of just sorted folders to make.
    """

    sorting_choice_dict = {}
    sorting_choice_list = []

    print("Please specify your folder name for each filetype as they appear.")
    for filetype in file_types:
        # print(filetype) #Debug
        current_choice = input("What category would you like to sort {} files into? ".format(filetype))
        sorting_choice_dict[filetype] = current_choice

        if current_choice not in sorting_choice_list:
            sorting_choice_list.append(current_choice)

    return sorting_choice_dict, sorting_choice_list


def make_sorted_directories(parent, directories):
    """
    Creates directories in parent directory.

    :param directories: List of directories to be made.
    :param parent: Parent directory for all directories to be made in.
    :return:
    """

    for directory in directories:
        final_path = os.path.join(parent, directory)
        if not os.path.isdir(final_path):
            os.mkdir(final_path)


main()
