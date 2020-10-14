import json
import os
import pickle
from collections import defaultdict
from itertools import combinations
from offline.autoCompleteData import AutoCompleteData


bad_chars = [';', ':', '-', '!', '*', ',', '$', '@']
data = defaultdict(set)
objects_list = []


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def read_file():
    for root, dirs, files in os.walk("../my_files/python-3.8.4-docs-text", topdown=True):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), encoding="utf8") as my_file:
                    sentences_list = my_file.read().split("\n")
                    for index, item in enumerate(sentences_list):
                        objects_list.append(AutoCompleteData(item, file, index + 1))

    with open('sentences.pkl', 'wb') as sentences:
        pickle.dump(objects_list, sentences)


def init_data():
    for index, sentence in enumerate(objects_list):
        count = 0
        substr_list = [sentence.completed_sentence[x:y] for x, y in combinations(range(len(sentence.completed_sentence) + 1), r=2)]
        for substr in substr_list:
            for char in bad_chars:
                substr = substr.replace(char, '')
            if not substr.startswith(" ") and not substr.endswith(" "):
                if count < 5:
                    data[substr.lower()].add(index)
                    count += 1

    with open("data.json", "w") as f:
        json.dump(data, f, cls=SetEncoder)


def print_data():
    for item in data:
        print(f'{item}: {data[item]}')


read_file()
init_data()

