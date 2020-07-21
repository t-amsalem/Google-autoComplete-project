from itertools import combinations
from collections import defaultdict

sent1 = "Hello big and beautiful world "
sent2 = "To be or not to be, This is the question"
sent3 = "Be good to everyone, everywhere, everytime"

sent_dict = {sent1: 0, sent2: 1, sent3: 2}
bad_chars = [';', ':', '!', '*', ',', '$', "@" " "]

data = defaultdict(set)


for sentence in sent_dict:
    substr_list = [sentence[x:y] for x, y in combinations(range(len(sentence) + 1), r=2)]
    for substr in substr_list:
        for char in bad_chars:
            substr = substr.replace(char, '')
        if not substr.startswith(" ") and not substr.endswith(" "):
            data[substr].add(sent_dict[sentence])


for item in data:
    print(f'{item}: {data[item]}')


