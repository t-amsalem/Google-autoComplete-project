import string
from collections import defaultdict
from string import ascii_lowercase
from online.load import data_, sentences_

best_sen = defaultdict(int)


def get_data_at_key(key):
    key = key.lower()
    sentences = []
    if key in data_:
        for k in data_[key]:
            sentences.append(sentences_[k])

    return sentences


def get_five_best_sentences(sub_str):
    best_sentences_dict = {}
    best_sentences = get_data_at_key(sub_str)

    for item in best_sentences:
        item.score = 2 * len(sub_str)

    if len(best_sentences) >= 5:
        return best_sentences[:5]

    else:
        result = replace_char(sub_str)

        for i in result:
            best_sentences_dict[i] = i.score
        result = delete_unnecessary_char(sub_str)

        for i in result:
            best_sentences_dict[i] = i.score
        result = add_missed_char(sub_str)

        for i in result:
            best_sentences_dict[i] = i.score

        a = set(sorted(best_sentences_dict, key=best_sentences_dict.get, reverse=False))
        a = set(best_sentences).union(a)

        return list(a)[:5]


def get_best_k_completions(sub_str):
    return get_five_best_sentences(sub_str)


def get_sentence_score(sentence):
    x = 0
    if sentence in data_.keys():
        x = len(sentence) * 2
    return max(x, replace_char(sentence)[1], delete_unnecessary_char(sentence)[1], add_missed_char(sentence)[1])


def replace_char(word):
    for index, char in enumerate(word):
        for letter in ascii_lowercase:
            if char != letter:
                new_word = word[:index] + letter + word[index+1:]
                if new_word in data_.keys():
                    score = (5 - index) if index < 5 else 1
                    score = (len(word) * 2) - score
                    result = get_data_at_key(new_word)
                    for item in result:
                        item.score = 0
                        if item not in best_sen:
                            item.score = score
                    return result
    return []


def delete_unnecessary_char(word):
    for index in range(1, len(word)-1):
        new_word = word[:index] + word[index + 1:]
        if new_word in data_.keys():
            score = (10 - 2 * index) if index < 4 else 2
            score = (len(word) * 2) - score
            result = get_data_at_key(new_word)
            for item in result:
                item.score = 0
                if item not in best_sen:
                    item.score = score
            return result
    return []


def add_missed_char(word):
    for index, char in enumerate(word):
        for letter in string.printable:
            new_word = word[:index] + letter + word[index:]
            if new_word in data_.keys():
                score = (10 - 2 * index) if index < 4 else 2
                score = (len(word) * 2) - score
                result = get_data_at_key(new_word)
                for item in result:
                    item.score = 0
                    if item not in best_sen:
                        item.score = score
                return result
    return []
