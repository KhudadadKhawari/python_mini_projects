from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter

def encrypt_pdf_func(filename, password):
    """
    Encrypts a PDF file with the given password.
    """
    try:
        reader = PdfFileReader(filename)
        filename = filename[:-4] + "_encrypted.pdf"
        with open(filename, 'wb') as f:
            writer = PdfFileWriter()
            writer.appendPagesFromReader(reader)
            writer.encrypt(password)
            writer.write(f)
        return filename
    except FileNotFoundError:
        raise FileNotFoundError


root = Tk()
root.minsize(width=600, height=400)
root.title("Encrypt PDF")


def open_file():
    filename = filedialog.askopenfilename(filetypes=(("PDF files","*.pdf"),("All files","*.*")))
    filename_label.config(text=filename)


def encrypt():
    file_loc = filename_label["text"]
    password_ = password.get().strip()
    try:
        encrypt_pdf_func(file_loc, password_)
        success_label.config(text="successfully encrypted!!")
        destination_label.config(text="destination: ")
        destination_file.config(text=file_loc[:-4] + "_encrypted.pdf")
    except FileNotFoundError:
        success_label.config(text="file not found")
        destination_label.config(text="destination: ")
        destination_file.config(text="")


label = Label(root, text="Select a PDF file to encrypt", font=20)
label.pack()

filename_label = Label(root, text="...", font=20)

open_file_button = Button(root, text="Open File", font=20, command=open_file)
open_file_button.pack()
filename_label.pack()

password_label = Label(root, text="Password", font=20)

password = Entry(root, width=30,  font=20)
password.insert(0, "Password")
password.pack()

success_label = Label(root, text="...", font=20)
success_label.pack()

encrypt_pdf = Button(root, text="Encrypt PDF", font=20, command=encrypt)
encrypt_pdf.pack()

destination_label = Label(root, text="", font=20)
destination_label.pack()
destination_file = Label(root, text="...", font=20)
destination_file.pack()

root.mainloop()