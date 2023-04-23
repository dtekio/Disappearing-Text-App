from tkinter import Tk, Text, Label, END
import re

timer = 0
has_written = False


def check_flag(event=None):
    global has_written

    if has_written:
        reset_timer()
    else:
        has_written = True
        countdown()


def reset_timer():
    global timer
    timer = 0


def countdown():
    global has_written

    if has_written:
        global timer
        timer += 1
        timer_label.config(text=timer)

        if timer >= 5:
            delete_text()
            has_written = False

        window.after(1000, countdown)


def delete_text():
    words = text_entry.get("1.0", "end-1c")
    wordcount = len(re.findall("\w+", words))

    timer_label.config(
        text=f"Your timer has ended. You've written {wordcount} words.")
    text_entry.delete("1.0", END)

    reset_timer()


window = Tk()

window.title("Disappearing Writing Text")

text_entry = Text(height=8, width=50)
timer_label = Label()

text_entry.bind("<Key>", check_flag)

text_entry.pack()
timer_label.pack()

# Main Loop
window.mainloop()
