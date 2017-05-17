"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Shaanan Braun'

TEMP_SAVE_FOLDER_NAME = "temp"
TOP_FOLDER_NAME = "Lyrics"


def main():
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir(TOP_FOLDER_NAME)

    if TEMP_SAVE_FOLDER_NAME not in os.listdir("."):
        os.mkdir(TEMP_SAVE_FOLDER_NAME)

    for dir_name, subdir_list, file_list in os.walk('.'):

        print(dir_name)

        if dir_name != '.' and dir_name != (".\\" + TEMP_SAVE_FOLDER_NAME):
            for filename in os.listdir(dir_name):
                if not os.path.isdir(filename):
                    # print(fix_filename(filename)) #Debug
                    shutil.copy(os.path.join(dir_name, filename), 'temp/' + fix_filename(filename))
    print("Renaming complete, files saved to: " + os.path.join(os.getcwd(), TEMP_SAVE_FOLDER_NAME))


def fix_filename(filename):
    temp_string = strip_file_extension(filename)
    # print(temp_string) #Debug
    temp_string[0] = split_uppercase_joined_words(temp_string[0])
    temp_string[0] = uppercase_words(temp_string[0])
    temp_string[0] = space_to_underscores(temp_string[0])
    temp_string[1] = temp_string[1].lower()

    return ".".join(temp_string)


def split_uppercase_joined_words(string):
    """
    Splits string at uppercase characters and returns string with each subsequent string seperated by a space.

    :param string:
    :return:
    """
    string_parts = string.split()
    string_split = []
    for word in string_parts:
        temp_word = ""
        for letter in word:
            if letter.isupper() and temp_word != "":  # When finding an uppercase letter split save word and start new word.
                if not temp_word[-1].isalpha():
                    if len(
                            temp_word) > 1:  # Only add previous word to list if it is not an empty string, ie has more than just the special character
                        string_split.append(temp_word[:-1])
                    temp_word = temp_word[-1]
                else:
                    string_split.append(temp_word)
                    temp_word = ""

            # print(temp_word)
            temp_word += letter
        string_split.append(temp_word)

    # print(name_split)  # debug
    return " ".join(string_split)


def uppercase_words(string):
    """
    Splits string and makes the first character of each word uppercase.

    :param string:
    :return:
    """
    string_parts = string.split()
    string_final = []
    for word in string_parts:
        id = 0
        for letter in word:
            if letter.isalpha():
                string_final.append(word[:id] + word[id].upper() + word[id + 1:])
                break
            id += 1


            # print(string_final) #Debug
    return " ".join(string_final)


def strip_file_extension(string):
    return string.split(".")


def space_to_underscores(string):
    return string.replace(" ", "_")


main()
