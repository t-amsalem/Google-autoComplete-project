from itertools import combinations
from collections import defaultdict

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
            for char in bad_chars:
                substr = substr.replace(char, '')
            if not substr.startswith(" ") and not substr.endswith(" "):
                data[substr].add(sent_dict[sentence])


def print_data():
    for item in data:
        print(f'{item}: {data[item]}')


def read_file():
    file = open("demofile.txt", "r")
    line = file.readline()

    file.close()


def get_best_k_completions(prefix):
    return List[AutoCompleteData]


class AutoCompleteData:
    def __init__(self, completed_sentence, source_text, offset, score):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def get_completed_sentence(self, ):
    def get_source_text(self, ):
    def get_offset(self, ):


    def replace_char(self, word):
        for char in word:
            for i in range(32, 67):
                if word.replace(char, chr(i)) in data.keys():
                    return i - 32
        return -1


    def delete_Unnecessary_char(self, word):
        for char in word:
            if word.replace(char, "") in data.keys():
              return word.index(char)
        return -1


    def add_missed_char(self, word):
        for char in word:
            for i in range(32, 67):
                if word.replace(char, char + chr(i)) in data.keys():
                    return i - 32
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

            self.score += (sentence.size() - 1) * 2

