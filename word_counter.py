from sys import argv

def word_count(file):
    """Tally the quantity of each unique word."""
    unique_words = dict()

    with open(input_file, "r") as text:
        for line in text:
            for word in line.split():
                if word in unique_words:
                    unique_words[word] += 1
                else:
                    unique_words[word] = 1
    return unique_words


def display(dictionary, key="word", reverse=True):
    ### MAKE THIS WORK WITH MULTIPLE CONTAINER TYPES ###
    """
    Displays each word and the quantity of that word within the file.

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


if __name__ == "__main__":
    script, input_file = argv
    display(word_count(input_file), key="qty")
