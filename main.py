from autoComplete import get_best_k_completions
from data import read_file, init_data


if __name__ == '__main__':
    print("Loading the files and preparing the system...")
    read_file()
    init_data()
    text = input("The system is ready, Enter your text: ")
    while True:
        if not text or "#" == text[-1]:
            print("Enter your text:")
            text = input()
        result = get_best_k_completions(text)
        i = len(result)
        print(f"There are {i} suggestions:")
        for index, item in enumerate(result):
            print(f'{index + 1}. {item.get_completed_sentence()} ({item.get_source_text()} {item.get_offset()})')
        print(text, end="")
        text += input()
