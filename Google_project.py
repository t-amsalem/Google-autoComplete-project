from itertools import combinations
from collections import defaultdict
from string import ascii_lowercase

# Mock data
# sent1 = "Hello big and beautiful world "
# sent2 = "To be or not to be, This is the question"
# sent3 = "Be good to everyone, everywhere, everytime"
# sent4 = "Good, better, best, never let them rest, Make the good better and the better make the best"
# sent5 = "Bee is making honey"
# sent6 = "We are learning in Beit - Yaakov"

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


def read_file(file_name):
    with open(file_name) as file:
        sentences_list = file.read().split("\n")
    for index1, item1 in enumerate(sentences_list):
        sent_dict[index1] = AutoCompleteData(item1, file_name, index1)


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
    if len(best_sentences) >= 5:
        for item in best_sentences:
            item.score = 2 * len(sub_str)
        return best_sentences[:5]
    else:
        for i in replace_char(sub_str)[0]:
            best_sen[i] = replace_char(sub_str)[1]
        for i in delete_unnecessary_char(sub_str)[0]:
            best_sen[i] = delete_unnecessary_char(sub_str)[1]
        for i in add_missed_char(sub_str)[0]:
            best_sen[i] = add_missed_char(sub_str)[1]
        a = set(sorted(best_sen, key=best_sen.get, reverse=True))
        a = set(best_sentences).union(a)
        return list(a)[:5]


def get_best_k_completions(sub_str):
    # info = []
    # best_sentences = get_five_best_sentences(sub_str)
    # for sentence in best_sentences:
    #     info.append()
    # return info
    return get_five_best_sentences(sub_str)

# # def get_sentence_score(sentence):
#
#
# # return sentence with high score
# def high_score_sentence(key):
#     result = get_data_at_key(key)
#     max_score = 0
#     sent_index = 0
#     for index, sentence in enumerate(result):
#         score = get_sentence_score(sentence)
#         if score > max_score:
#             max_score = score
#             sent_index = index
#     return result[sent_index]


def get_sentence_score(sentence):
    x = 0
    if sentence in data.keys():
        x = len(sentence) * 2
    return max(x, replace_char(sentence)[1], delete_unnecessary_char(sentence)[1], add_missed_char(sentence)[1])


def replace_char(word):
    for index, char in enumerate(word):
        for i in ascii_lowercase:
            if word.replace(char, i, 1) in data.keys():
                if index < 5:
                    score = 5 - index
                else:
                    score = 1
                score = (len(word) * 2) - score
                return get_data_at_key(word.replace(char, i, 1)), score
    return [], 0


def delete_unnecessary_char(word):
    for index, char in enumerate(word):
        if word.replace(char, "", 1) in data.keys():
            if index < 4:
                score = 10 - 2 * index
            else:
                score = 2
            score = (len(word) * 2) - score
            return get_data_at_key(word.replace(char, "", 1)), score
    return [], 0


def add_missed_char(word):
    for index, char in enumerate(word):
        for i in ascii_lowercase:
            if word.replace(char, char + i, 1) in data.keys():
                if index < 4:
                    score = 10 - 2 * index
                else:
                    score = 2
                score = (len(word) * 2) - score
                return get_data_at_key(word.replace(char, char + i, 1)), score
    return [], 0


if __name__ == '__main__':
    print("Loading the files and preparing the system...")
    read_file("about.txt")
    init_data()
    text = input("The system is ready, Enter your text: ")
    while text != '#':
        result = get_best_k_completions(text)
        i = len(result)
        print(f"There are {i} suggestions:")
        for index, item in enumerate(result):
            print(f'{index + 1}. {item.get_completed_sentence()} ({item.get_source_text()} {item.get_offset()})')
            # print(item.get_score())
        print(text)
        text = input()