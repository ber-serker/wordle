# import json
# five_word = {}
# with open("words_dictionary.json", "r") as data:
#     data_file = json.load(data)
#     for i in data_file:
#         if len(i) == 5:
#             five_word[i] = 1
# with open("ff.txt", "w") as file2:
#     file2.write(json.dumps(five_word))

from tkinter import *

from json import *

with open("ff.txt", "r") as file1:
    LIST1 = load(file1)


def correct_letter(list1, letter1, place):
    listx = []
    for i in list1:
        if i[place] == letter1:
            listx.append(i)

    return listx


def wrong_pos(list1, letter1, place):
    listx = []
    for i in list1:
        if letter1 in i:
            if i[place] != letter1:
                listx.append(i)

    return listx


def wrong_letter(listx, x):
    list1=[]
    for i in listx:
        br=False
        for j in x:
            if j in i:
                br=True
                break
        if br:
            continue
        else:
            list1.append(i)

    return list1


def search_but():
    listy = LIST1
    if correct_entry1.index("end") != 0:
        listy = correct_letter(LIST1, correct_entry1.get(), 0)
    if correct_entry2.index("end") != 0:
        listy = correct_letter(listy, correct_entry2.get(), 1)
    if correct_entry3.index("end") != 0:
        listy = correct_letter(listy, correct_entry3.get(), 2)
    if correct_entry4.index("end") != 0:
        listy = correct_letter(listy, correct_entry4.get(), 3)
    if correct_entry5.index("end") != 0:
        listy = correct_letter(listy, correct_entry5.get(), 4)
    if wrong_entry1.index("end") != 0:
        listy = wrong_pos(listy, wrong_entry1.get(), 0)
    if wrong_entry2.index("end") != 0:
        listy = wrong_pos(listy, wrong_entry2.get(), 1)
    if wrong_entry3.index("end") != 0:
        listy = wrong_pos(listy, wrong_entry3.get(), 2)
    if wrong_entry4.index("end") != 0:
        listy = wrong_pos(listy, wrong_entry4.get(), 3)
    if wrong_entry5.index("end") != 0:
        listy = wrong_pos(listy, wrong_entry5.get(), 4)

    g = '\n'.join(wrong_letter(listy, wl_entry.get()))

    result_box.delete("1.0", "end")
    result_box.insert(END, g)


window = Tk()
window.title("Wordle Cheat")
window.config(padx=50, pady=50)

canvas_logo = Canvas(width=200, height=200)
logo_image = PhotoImage(file="wordle.PNG")
canvas_logo.create_image(100, 100, image=logo_image)
canvas_logo.grid(row=0, column=1, columnspan=3)

correct_label = Label(text="Correct Position: ")
correct_label.grid(row=1, column=0)

wrong_label = Label(text="Wrong Position: ")
wrong_label.grid(row=2, column=0)

wl_label = Label(text="Wrong Letters: ")
wl_label.grid(column=0, row=3)

wl_entry = Entry(width=10)
wl_entry.grid(column=1, row=3)

correct_entry1 = Entry(width=2)
correct_entry1.grid(row=1, column=1)

correct_entry2 = Entry(width=2)
correct_entry2.grid(row=1, column=2)

correct_entry3 = Entry(width=2)
correct_entry3.grid(row=1, column=3)

correct_entry4 = Entry(width=2)
correct_entry4.grid(row=1, column=4)

correct_entry5 = Entry(width=2)
correct_entry5.grid(row=1, column=5)

wrong_entry1 = Entry(width=2)
wrong_entry1.grid(row=2, column=1)

wrong_entry2 = Entry(width=2)
wrong_entry2.grid(row=2, column=2)

wrong_entry3 = Entry(width=2)
wrong_entry3.grid(row=2, column=3)

wrong_entry4 = Entry(width=2)
wrong_entry4.grid(row=2, column=4)

wrong_entry5 = Entry(width=2)
wrong_entry5.grid(row=2, column=5)

search_button = Button(text="search", bg="Red", command=search_but)
search_button.grid(row=3, column=2)

result_box = Text(width=50, height=10)
result_box.grid(row=4, column=0, columnspan=6)

window.mainloop()
