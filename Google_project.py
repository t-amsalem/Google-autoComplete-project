from itertools import combinations
from collections import defaultdict
from string import ascii_lowercase
import os


sent_dict = {}
bad_chars = [';', ':', '-', '!', '*', ',', '$', '@']
data = defaultdict(set)
best_sen = defaultdict(int)


class AutoCompleteData:
    def __init__(self, sentence, source_text, offset):
        self.completed_sentence = sentence
        self.source_text = source_text
        self.offset = offset
        self.score = 0
    def get_completed_sentence(self):
        return self.completed_sentence
    def get_source_text(self):
        return self.source_text
    def get_offset(self):
        return self.offset
    def get_score(self):
        return self.score


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


def get_five_best_sentences(sub_str):
    best_sentences = get_data_at_key(sub_str)
    for item in best_sentences:
        item.score = 2 * len(sub_str)
    if len(best_sentences) >= 5:
        return best_sentences[:5]
    else:
        for i in replace_char(sub_str)[0]:
            best_sen[i] = i.score
        for i in delete_unnecessary_char(sub_str)[0]:
            best_sen[i] = i.score
        for i in add_missed_char(sub_str)[0]:
            best_sen[i] = i.score
        a = set(sorted(best_sen, key=best_sen.get, reverse=True))
        a = set(best_sentences).union(a)
        for item in list(a):
            print(item.score)
        return list(a)[:5]


def get_best_k_completions(sub_str):
    return get_five_best_sentences(sub_str)


def get_sentence_score(sentence):
    x = 0
    if sentence in data.keys():
        x = len(sentence) * 2
    return max(x, replace_char(sentence)[1], delete_unnecessary_char(sentence)[1], add_missed_char(sentence)[1])


def replace_char(word):
    for index, char in enumerate(word):
        for i in ascii_lowercase:
            if word.replace(char, i, 1) in data.keys():
                score = (5 - index) if index < 5 else 1
                score = (len(word) * 2) - score
                for item in result:
                    if item not in best_sen:
                        item.score = score
                return result
                # return get_data_at_key(word.replace(char, i, 1)), score
    # return [], 0


def delete_unnecessary_char(word):
    for index, char in enumerate(word):
        if word.replace(char, "", 1) in data.keys():
            score = (10 - 2 * index) if index < 4 else 2
            score = (len(word) * 2) - score
            return get_data_at_key(word.replace(char, "", 1)), score
    return [], 0


def add_missed_char(word):
    for index, char in enumerate(word):
        for i in ascii_lowercase:
            if word.replace(char, char + i, 1) in data.keys():
                score = (10 - 2 * index) if index < 4 else 2
                score = (len(word) * 2) - score
                return get_data_at_key(word.replace(char, char + i, 1)), score
    return [], 0


if __name__ == '__main__':
    print("Loading the files and preparing the system...")
    read_file()
    init_data()
    text = input("The system is ready, Enter your text: ")
    while text != '#':
        result = get_best_k_completions(text)
        i = len(result)
        print(f"There are {i} suggestions:")
        for index, item in enumerate(result):
            print(f'{index + 1}. {item.get_completed_sentence()} ({item.get_source_text()} {item.get_offset()})')
        print(text)
        text = input()
