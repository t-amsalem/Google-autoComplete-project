
sent1 = "Hello big and beautiful world "
sent2 = "To be or not to be, This is the question and"
sent3 = "Be good to everyone, everywhere, everytime"

sent_dict = [sent1, sent2, sent3]
bad_chars = [';', ':', '!', "*", ",", "$", "@"]

data = {}


for sentence in sent_dict:
    new_sentence = sentence.split()
    for word in new_sentence:
        if word not in data:
            for i in bad_chars:
                word = word.replace(i, '')
            data[word.lower()] = sentence
        else:
            if data[word.lower()] != sentence:
                data[word.lower()] += ", "
                data[word.lower()] += sentence


# word = "hello"
# if word in data:
#     print(data[word])

for item in data:
    print(f'{item}: {data[item]}')

# print(data)
