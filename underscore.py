import tkinter
import pyperclip

# Functions are here.
def underscore():
    # Get text.
    #text = input("Underscore: ").
    text = entry.get()

    # Add an underscore between every letter and number.
    text = text.lower()
    underscored_text = ""

    for i in text:
        if i.isalpha():
            underscored_text += i
        else:
            underscored_text += "_" + i + "_"

    # Removes double underscore -> two digits one after another.
    underscored_text = underscored_text.replace("__", "")

    # Removes _ if it is the last char of the string.
    if underscored_text[-1] == "_":
        underscored_text = underscored_text[:-1]


    # print(underscored_text).
    pyperclip.copy(underscored_text)



main_window = tkinter.Tk()

# Label.
label = tkinter.Label(main_window, text="Underscore:")
label.grid(row=0, column=1)

# Entry box.
var = tkinter.StringVar()
var.set(pyperclip.paste())
entry = tkinter.Entry(main_window, textvariable=var)
entry.grid(row=0, column=2)

# Calls underscore().
button = tkinter.Button(main_window, text = "Do it", command = underscore)
button.grid(row=1, column=2)

tkinter.mainloop()


