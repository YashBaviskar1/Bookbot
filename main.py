

def main():
    path = 'books/frankenstein.txt'
    with open(path) as f :
        file_contents = f.read()
    print(f"--- Begin Book Report of {path} ---")
    print("no of words in this books is : ", no_of_words(file_contents))
    count_print(no_of_letters(file_contents))
    print("--- End report ---")


def no_of_words(text):
    words = text.split()
    return len(words)


def no_of_letters(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    words = text.lower()
    set_of_letter = set(letters)
    count_of_letter = {}
    for letter in set_of_letter:
        count_of_letter[letter] = words.count(letter)
    

    return count_of_letter


def sort_on(dict):
    for i in dict:
        return dict[i]

def count_print(dict):
    list_of_dict = []

    for i in dict:
        temp_dict = {}
        temp_dict[i] = dict[i]
        list_of_dict.append(temp_dict)
    list_of_dict.sort(reverse=True, key=sort_on)

    for i in range(len(list_of_dict)):
        for key, val in list_of_dict[i].items():
            print(f"the '{key}' character was found {val} times ")

    
        



if __name__ == '__main__':
    main()