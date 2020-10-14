from tkinter import *
from online.autoComplete import get_best_k_completions


def clear():
    if text.get(1.0, END):
        text.delete(1.0, END)


master = Tk()

label = Label(master, text="The system is ready, Enter your text: ", fg='purple').pack(side=TOP)

master.title("Auto - completions")
e = Entry(master,
          width=20,
          background='lightgoldenrodyellow')

e.pack()


text = Text(master,
            width=100,
            background='cornsilk',
            fg='indigo')


text.pack()


def main_program():
    prefix = e.get()  # This is the text you may want to use later
    fixed_prefix = prefix

    result = 'Your string is: ' + fixed_prefix + '\n'

    if fixed_prefix:
        clear()
        suggestions = get_best_k_completions(prefix)
        num = len(suggestions)
        result += "\n ********************************************************* \n"

        if suggestions:
            result += f"There are {num} suggestion to \'{fixed_prefix}\': \n"

            for index, item in enumerate(suggestions):
                result += f'{index + 1}. {item.get_completed_sentence()} ' \
                          f'({item.get_source_text()} ' \
                          f'{item.get_offset()}) \n'

        else:
            result += "\tThere are no suggestions"

        result += "\n ********************************************************* \n "
        text.insert(INSERT, result)
        text.pack()


search_button = Button(master,
                       text="Search",
                       command=main_program,
                       background='moccasin',
                       foreground='purple',
                       activebackground='pink',
                       activeforeground='purple')

search_button.pack(side=LEFT)


close_button = Button(master,
                      text="Close",
                      command=master.quit,
                      background='moccasin',
                      foreground='purple',
                      activebackground='pink',
                      activeforeground='purple')

close_button.pack(side=RIGHT)


mainloop()



