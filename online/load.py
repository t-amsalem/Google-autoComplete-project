import json
import pickle


def load_text_sources():
    print("Loading the files and preparing the system...")

    with open("../offline/data.json", "r") as data_file:
        data = json.load(data_file)

    with open("../offline/sentences.pkl", "rb") as sentences_file:
        sentences = pickle.load(sentences_file)

    return data, sentences


data_, sentences_ = load_text_sources()
