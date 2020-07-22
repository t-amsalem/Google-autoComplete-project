from itertools import combinations
from collections import defaultdict
from string import ascii_lowercase


sent1 = "Hello big and beautiful world "
sent2 = "To be or not to be, This is the question"
sent3 = "Be good to everyone, everywhere, everytime"

sent_dict = {sent1: 0, sent2: 1, sent3: 2}
bad_chars = [';', ':', '!', '*', ',', '$', "@" " "]

data = defaultdict(set)

def init_data():
    for sentence in sent_dict:
        substr_list = [sentence[x:y] for x, y in combinations(range(len(sentence) + 1), r=2)]
        for substr in substr_list:
            # substr = substr.lower()
            for char in bad_chars:
                substr = substr.replace(char, '')
            if not substr.startswith(" ") and not substr.endswith(" "):
                data[substr.lower()].add(sent_dict[sentence])


def print_data():
    for item in data:
        print(f'{item}: {data[item]}')


# def read_file():
#     file = open("demofile.txt", "r")
#     line = file.readline()
#
#     file.close()


# def get_best_k_completions(prefix):
#     info = []
#     info.append()
#     return List[AutoCompleteData]


def get_Data_at_key(key):
    key = key.lower()
    sentences = []
    for k in data[key]:
        sentences.append(list(sent_dict.keys())[k])
    return sentences


class AutoCompleteData:
    def __init__(self):
        self.completed_sentence = ""
        self.source_text = ""
        self.offset = 0
        self.score = 0


# return the sentence with the high score
    def get_completed_sentence(self, key):
        result = get_Data_at_key(key)
        max_score = 0
        sent_index = 0
        for index, sentence in enumerate(result):
            score = self.get_score(sentence)
            if score > max_score:
                max_score = score
                sent_index = index
        return result[sent_index]

    # def get_source_text(self, ):

    # def get_offset(self, ):

    def replace_char(self, word):
        for index, char in enumerate(word):
            for i in ascii_lowercase:
                if word.replace(char, i) in data.keys():
                    return index
        return -1

    def delete_Unnecessary_char(self, word):
        for char in word:
            if word.replace(char, "") in data.keys():
              return word.index(char)
        return -1

    def add_missed_char(self, word):
        for index, char in enumerate(word):
            for i in ascii_lowercase:
                if word.replace(char, char + i) in data.keys():
                    return index + 1
        return -1

    def get_score(self, sentence):
        sentence = sentence.split()
        for word in sentence:
            if self.replace_char(word) != -1:
                index = self.replace_char(word)
                if index < 6:
                    self.score -= (5 - index % 5)
                else:
                    self.score -= 1

            elif self.delete_Unnecessary_char(word) != -1 or self.add_missed_char(word) != -1:
                    index = self.delete_Unnecessary_char(word)
                    if index < 5:
                        self.score -= (10 - index % 5)
                    else:
                        self.score -= 2
            else:
                self.score += len(word) * 2

        self.score += (len(sentence) - 1) * 2
        return self.score


# Tests:
# init_data()
# print_data()
# print(get_Data_at_key("Be"))
# acd = AutoCompleteData()
# print(acd.get_completed_sentence("to"))
# print(acd.replace_char("kello"))
# print(acd.delete_Unnecessary_char("helplo"))
# print(acd.add_missed_char("helo"))
# print(acd.get_score("be"))
