from sys import argv
import re

def word_count(file):
    """Tally the quantity of each unique word."""
    unique_words = dict()
    delimiters = (',', ' ', '.', ';', '\n', '\'', "!", "(", ")", "-", \
                  "—", "?", "\"", ":", "@", "#", "$", "*", "•")
    pattern = "|".join(map(re.escape, delimiters))
    # print(pattern)

    with open(file, "r") as text:
        un_punct = re.split(pattern, text.read())
    #     print(un_punct)
        for word in un_punct:
            if len(word) == 0:
                pass
            elif word in unique_words:
                unique_words[word] += 1
            else:
                unique_words[word] = 1
    return unique_words

def display(dictionary, key="word", reverse=True):
    ### MAKE THIS WORK WITH MULTIPLE CONTAINER TYPES ###
    """
    Displays each word and the quantity of that word within the file
    with format:

    word    count
    word    count
    etc.

    Arguments:
    iterable -- a dictionary of word, quantity pairs

    Optional arguments:
    key -- sets the left-most column data type
    reverse -- if set, sorts list in descending order
    """

    sorted_by_qty = sorted(((value, key) for key, value in dictionary.items()), reverse=reverse)

    for item in sorted_by_qty:
        if key == "qty":
            print("{}\t{}".format(item[0], item[1]))
        elif key == "word":
            print("{}\t{}".format(item[1], item[0]))

    print("Total words: {}".format(sum(v for k, v in dictionary.items())))

def write_to_file(dictionary, save_file, key="word", reverse=True):
    ### MAKE THIS WORK WITH MULTIPLE CONTAINER TYPES ###
    """
    Writes a list of each word and the quantity of that word within the file
    with format:

    word,count
    word,count
    etc.

    Arguments:
    iterable -- a dictionary of word, quantity pairs

    Optional arguments:
    key -- sets the left-most column data type
    reverse -- if set, sorts list in descending order
    """

    sorted_by_qty = sorted(((value, key) for key, value in dictionary.items()), reverse=reverse)

    with open(save_file, "w") as new_file:
        for item in sorted_by_qty:
            if key == "qty":
                new_file.write("{},{}\n".format(item[0], item[1]))
            elif key == "word":
                new_file.write("{},{}\n".format(item[1], item[0]))


if __name__ == "__main__":
    script, input_file = argv
    display(word_count(input_file), key="qty")
