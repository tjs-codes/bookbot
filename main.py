# Asks the user to input a text-file (a book, for example)
# Opens the text file and reads contents into a variable
# Then uses a method to count the words and letters; then prints out a result
def main():
    file_path = input("Please enter the path of the text file: ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at the specified path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    word_number = count_words(content)
    letter_dictionary = count_letters(content)
    sorted_letter_list = sort_letter_list(letter_dictionary)
    print(f"--- Begin report of {file_path} ---")
    print(f"This book has {word_number} words.")
    print()
    for item in sorted_letter_list:
        print(f"The {item['char']} character was found {item['num']} times")
    print(f"--- End report ---")

# Counts the number of words
# Splits the full book string on whitespaces, makes a list and returns the length of that list
def count_words(book):
    words_list = book.split()
    word_count = len(words_list)
    return word_count

# Counts the number of letters
# Loops through the characters in the book and stores the number of each char in a dictionary
# Only accepts alphabetical characters
def count_letters(book):
    letters_dict = {}
    for char in book:
        char = char.lower()
        if char != " " and char.isalpha():
            if char in letters_dict:
                letters_dict[char] += 1
            else:
                letters_dict[char] = 1
    return letters_dict

# Sorting helper method
def sort_on(d):
    return d["num"]

# Takes the unsorted letter dictionary and turns it into a sortable list
def sort_letter_list(unsorted_dict):
    sorted_letter_list = []
    for char in unsorted_dict:
        sorted_letter_list.append({"char": char, "num": unsorted_dict[char]})
    sorted_letter_list.sort(reverse=True, key=sort_on)
    return sorted_letter_list

main()