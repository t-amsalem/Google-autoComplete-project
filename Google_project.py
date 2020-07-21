
sent1 = "Hello big and beautiful world "
sent2 = "To be or not to be, This is the question and"
sent3 = "Be good to everyone, everywhere, everytime"

sent_dict = [sent1, sent2, sent3]
bad_chars = [';', ':', '!', "*", ",", "$", "@"]

data = {}


# for sentence in sent_dict:
#     new_sentence = sentence.split()
#     # set_sent = set(new_sentence)
#     for word in new_sentence:
#         for i in bad_chars:
#             word = word.replace(i, '')
#         if word not in data:
#             # data[word.lower()] = sentence
#             # set_sent = set(sentence)
#             data[word.lower()] = sentence
#             # set_sent.add(data[word.lower()])
#         else:
#             # if data[word.lower()] != sentence:
#                 # data[word.lower()] += ", "
#                 # data[word.lower()] += sentence
#             # if data[word.lower()] not in set_sent:
#             # a = data[word.lower()] + sentence
#             # print(f'aaaa{a}')
#             # print(type(a))
#             print(type(data[word.lower()]))
#             print(type(sentence))
#
#             # d = set(a)
#             data[word.lower()] = set(list(data[word.lower()]).append(sentence))
#             print(type(data[word.lower()]))
#
#                 # set_sent.add(data[word.lower()])
# for sentence in sent_dict:
#     new_sentence = sentence.split()
#     for word in new_sentence:
#         for i in bad_chars:
#             word = word.replace(i, '')
#         if word not in data:
#             data[word.lower()] = sentence
#         else:
#             if data[word.lower()] != sentence:
#                 data[word.lower()] = data[word.lower()] + ", " + sentence


for sentence in sent_dict:
    for i in range(len(sentence)):
        shortSen = sentence[:i]
        if not shortSen.endswith(" "):
            data[shortSen] = sentence


# word = "hello"
# if word in data:
#     print(data[word])

for item in data:
    print(f'{item}: {data[item]}')

# print(data)
