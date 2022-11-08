import pyttsx3, PyPDF2, sys
from tkinter import Tk, filedialog, Label, Button


def select_file():
    filetypes = (
        ('pdf files', '*.pdf'),
    )

    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    speaker = pyttsx3.init()

    the_pdf = open(f"{filename}", "rb")
    reader = PyPDF2.PdfFileReader(the_pdf)

    for i in range(reader.getNumPages()):
        page = reader.getPage(i)
        content = page.extract_text()

        speaker.say(content)
        speaker.runAndWait()


window = Tk()
window.geometry("700x200+400+100")
window.title("PDF READER")
window.config(padx=30, pady=50, bg="#FFFAD7")

open_button = Button(
    window,
    text='Open a File',
    command=select_file
)

open_button.grid(row=0, column=0)

file_path = Label(text="", font=("TIMES", 10, "bold"))
file_path.grid(row=1, column=0, pady=20)

warn = Label(text="If the program is reading the pdf and you want to stop it, simply kill the terminal.", fg="red", bg="#FFFAD7", font=("Cooper Std Black", 13, "bold"))
warn.grid(row=1, column=0)

window.mainloop()