"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Shaanan Braun'


def main():
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    # print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
            split_uppercase_joined_words(filename)
            print(new_name)

            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)


            # Processing subdirectories using os.walk()
            # os.chdir('..')
            # for dir_name, subdir_list, file_list in os.walk('.'):
            #     print("In", dir_name)
            #     print("\tcontains subdirectories:", subdir_list)
            #     print("\tand files:", file_list)


def fix_name(name):
    return name


def split_uppercase_joined_words(name):
    name_parts = name.split()
    name_split = []
    for word in name_parts:
        temp_word = ""
        for letter in word:
            if letter.isupper() and temp_word != "": #When finding an uppercase letter split save word and start new word.
                if not temp_word[-1].isalpha():
                    if len(temp_word) > 1: #Only add previous word to list if it is not an empty string, ie has more than just the special character
                        name_split.append(temp_word[:-1])
                    temp_word = temp_word[-1]
                else:
                    name_split.append(temp_word)
                    temp_word = ""

            print(temp_word)
            temp_word += letter
        name_split.append(temp_word)
    print(name_split)  # debug
    return name_split


def space_to_underscores(name):
    return name.replace(" ", "_")


main()
