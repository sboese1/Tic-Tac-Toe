from tkinter import *

count = 0

def win():
    if button_one["text"] != "" and (button_one["text"] == button_two["text"] == button_three["text"]):
        if button_one["text"] == "X":
            print("Player X wins!")
        else:
            print("Player O wins!")
        root.destroy()
    elif button_four["text"] != "" and (button_four["text"] == button_five["text"] == button_six["text"]):
        if button_four["text"] == "X":
            print("Player X wins!")
        else:
            print("Player O wins!")
        root.destroy()
    elif button_seven["text"] != "" and (button_seven["text"] == button_eight["text"] == button_nine["text"]):
        if button_seven["text"] == "X":
            print("Player X wins!")
        else:
            print("Player O wins!")
        root.destroy()
    elif button_one["text"] != "" and (button_one["text"] == button_four["text"] == button_seven["text"]):
        if button_one["text"] == "X":
            print("Player X wins!")
        else:
            print("Player O wins!")
        root.destroy()
    elif button_two["text"] != "" and (button_two["text"] == button_five["text"] == button_eight["text"]):
        if button_two["text"] == "X":
            print("Player X wins!")
        else:
            print("Player O wins!")
        root.destroy()
    elif button_three["text"] != "" and (button_three["text"] == button_six["text"] == button_nine["text"]):
        if button_three["text"] == "X":
            print("Player X wins!")
        else:
            print("Player O wins!")
        root.destroy()
    elif button_one["text"] != "" and (button_one["text"] == button_five["text"] == button_nine["text"]):
        if button_one["text"] == "X":
            print("Player X wins!")
        else:
            print("Player O wins!")
        root.destroy()
    elif button_three["text"] != "" and (button_three["text"] == button_five["text"] == button_seven["text"]):
        if button_one["text"] == "X":
            print("Player X wins!")
        else:
            print("Player O wins!")
        root.destroy()

def move(num):
    turn = "X"
    global count
    if count % 2 == 0:
        turn = "O"

    if num == 1:
        button_one.config(text=turn)
        button_one["state"] = "disabled"
    elif num == 2:
        button_two.config(text=turn)
        button_two["state"] = "disabled"
    elif num == 3:
        button_three.config(text=turn)
        button_three["state"] = "disabled"
    elif num == 4:
        button_four.config(text=turn)
        button_four["state"] = "disabled"
    elif num == 5:
        button_five.config(text=turn)
        button_five["state"] = "disabled"
    elif num == 6:
        button_six.config(text=turn)
        button_six["state"] = "disabled"
    elif num == 7:
        button_seven.config(text=turn)
        button_seven["state"] = "disabled"
    elif num == 8:
        button_eight.config(text=turn)
        button_eight["state"] = "disabled"
    elif num == 9:
        button_nine.config(text=turn)
        button_nine["state"] = "disabled"

    win()
    count = count + 1
    if count == 9:
        print("The result is a tie!")
        root.destroy()

root = Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

frame = Frame(root)
frame.grid(row=0, column=0, sticky="news")

button_one = Button(master=frame, command=lambda: move(1))
button_one.grid(row=0, column=0, sticky="news")

button_two = Button(master=frame, command=lambda: move(2))
button_two.grid(row=0, column=1, sticky="news")

button_three = Button(master=frame, command=lambda: move(3))
button_three.grid(row=0, column=2, sticky="news")

button_four = Button(master=frame, command=lambda: move(4))
button_four.grid(row=1, column=0, sticky="news")

button_five = Button(master=frame, command=lambda: move(5))
button_five.grid(row=1, column=1, sticky="news")

button_six = Button(master=frame, command=lambda: move(6))
button_six.grid(row=1, column=2, sticky="news")

button_seven = Button(master=frame, command=lambda: move(7))
button_seven.grid(row=2, column=0, sticky="news")

button_eight = Button(master=frame, command=lambda: move(8))
button_eight.grid(row=2, column=1, sticky="news")

button_nine = Button(master=frame, command=lambda: move(9))
button_nine.grid(row=2, column=2, sticky="news")

for i in range(3):
    Grid.rowconfigure(frame, i, weight=1)
    for j in range(3):
        Grid.columnconfigure(frame, j, weight=1)

root.mainloop()