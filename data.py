import os
from collections import defaultdict
from itertools import combinations
from autoCompleteData import AutoCompleteData


bad_chars = [';', ':', '-', '!', '*', ',', '$', '@']
sent_dict = {}
data = defaultdict(set)


def read_file():
    for root, dirs, files in os.walk("./my_files/python-3.8.4-docs-text/", topdown=True):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), encoding="utf8") as my_file:
                    sentences_list = my_file.read().split("\n")
                    for index1, item1 in enumerate(sentences_list):
                        sent_dict[index1] = AutoCompleteData(item1, file, index1)


def init_data():
    for index, sentence in sent_dict.items():
        substr_list = [sentence.completed_sentence[x:y] for x, y in combinations(range(len(sentence.completed_sentence) + 1), r=2)]
        for substr in substr_list:
            for char in bad_chars:
                substr = substr.replace(char, '')
            if not substr.startswith(" ") and not substr.endswith(" "):
                data[substr.lower()].add(index)


def print_data():
    for item in data:
        print(f'{item}: {data[item]}')


def get_data_at_key(key):
    key = key.lower()
    sentences = []
    for k in data[key]:
        sentences.append(sent_dict[k])
    return sentences
