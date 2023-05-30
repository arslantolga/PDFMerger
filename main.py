from tkinter import filedialog
import tkinter
from pathlib import Path
from PyPDF2 import PdfMerger

FONT = ('Helvetica', 12)

window = tkinter.Tk()
window.title("PDF Merging")
window.geometry("300x200")

def choose():
    merger = PdfMerger()
    pdf_files = []
    filenames = filedialog.askopenfilenames()

    if filenames:
        for filename in filenames:
            pdf_files.append(filename)

        ana_dizin = pdf_files[0]
        ayrilmis = ana_dizin.split("/")
        del ayrilmis[-1]
        birlesik = "/".join(ayrilmis)

        for pdf_file in pdf_files:
            merger.append(pdf_file)
        merger.write(f"{birlesik}/merge.pdf")
        merger.close()
        label_result.config(text="Merged File Created!")
        label_result.pack()
    else:
        print("No files selected.")


label = tkinter.Label(text="Choose PDF Files", font=FONT, pady=30)
label.pack()

button_choose = tkinter.Button(text="Choose", command=choose)
button_choose.pack()

label_result = tkinter.Label(font=FONT, pady=30)

window.mainloop()


