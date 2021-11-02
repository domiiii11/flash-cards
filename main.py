import tkinter as tk
import pandas as pd
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()
window.title("Flash cards will help you to memorize anything!")
window.config(height=400, width=600, bg="#d3ffce")
sec = 5


word_label = tk.Label(window, borderwidth=0, text="blah", anchor='center', bg="#64a279", font="Verdana 30 bold")
word_label.place(relx=0.5, rely=0.5, anchor='center', height=330, width=540)

# frame1 = ttk.Frame(style="RoundedFrame", padding=10)

time_label = tk.Label(window)
time_label.place(relx=0.5, rely=0.75, anchor='center')
counter = 0

csvFile = pd.read_csv('./data/french_words.csv')
data = pd.read_csv('./data/french_words.csv', usecols=["French", "English"])
print(data)
var = tk.IntVar()

language_label = tk.Label(window, text="French", anchor='center', bg="#64a279",
                          font="Verdana 10 bold")
language_label.place(relx=0.5, rely=0.2, anchor='center')

def delete_from_list(countr):
    global data
    data = data.drop(countr)


button_yes_image = tk.PhotoImage(file="./tick.png")
button_yes = tk.Button(window, text="Yes", command=lambda: var.set(1), image=button_yes_image)
button_yes.place(relx=0.2, rely=0.8, anchor="center")

button_no_image = tk.PhotoImage(file="./x.png")
button_no = tk.Button(window, text="No", command=lambda: var.set(1), image=button_no_image)
button_no.place(relx=0.8, rely=0.8, anchor="center")


def count_time(label):
    global sec
    global counter
    if var.get() == 1:
        guessed(label)
    timer = '{:2d}'.format(sec)
    label["text"] = timer
    sec -= 1
    if sec == -1:
        guessed(label)
    label.after(1000, lambda: count_time(label))


def guessed(label):
    global sec
    show_english_meaning()
    label["text"] = "Was it right answer?"
    button_yes.wait_variable(var)
    if var.get() == 1:
        delete_from_list(counter)
    sec = 5
    next_word()
    var.set(2)


def next_word():
    global counter
    counter += 1
    language_label["text"] = "French"
    word_label["text"] = data["French"][counter]
    word_label["bg"] = "#64a279"
    language_label["bg"] = "#64a279"


def show_english_meaning():
    global counter
    language_label["text"] = "English"
    word_label["text"] = data["English"][counter]
    word_label["bg"] = "#2a7c5c"
    language_label["bg"] = "#2a7c5c"


def save_accomplisment():
    data.to_csv("file1.csv")


def saving_prompt():
    answer = tk.messagebox.askyesnocancel(title="Question", message="Would like to save your progress?")
    if answer:
        save_accomplisment()
        window.destroy()
    elif answer == False:
        window.destroy()
        print(answer)


def run_programme():
    next_word()
    count_time(time_label)
    window.protocol('WM_DELETE_WINDOW', saving_prompt)


run_programme()

window.mainloop()
