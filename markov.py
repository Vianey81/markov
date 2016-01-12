from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    string_file = open(file_path).read()

    return string_file


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """


    chains = {}
    all_words = text_string.split()
    for index in range(0, len(all_words)-2):
        bi_gram = (all_words[index], all_words[index+1])
        next_word = all_words[index+2]
        if bi_gram in chains:
            chains[bi_gram].append(next_word)
        else:
            chains[bi_gram] = [next_word]  

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    all_upper_tuples = []
    for a_tuple in chains.keys():
        if a_tuple[0][0].isupper():
            all_upper_tuples.append(a_tuple)
    current_tuple = choice(all_upper_tuples)
    text += current_tuple[0] + " " + current_tuple[1] + " "

    end_punctuation = [".", "?", "!"]
    while current_tuple in chains and current_tuple[1][-1] not in end_punctuation:
        rand_word = choice(chains[current_tuple])
        text += rand_word + " "
        current_tuple = (current_tuple[1], rand_word)

    return text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
