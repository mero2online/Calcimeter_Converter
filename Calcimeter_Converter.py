from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pandas import DataFrame
import os

from HelperFunc import checkInputFile, resource_path

try:
    import pyi_splash  # type: ignore
    pyi_splash.close()
except:
    pass

filetypes = (
    ('All files', '*.*'),
    ('XLSX EXCEL files', '*.xlsx'),
    ('XLS EXCEL files', '*.xls'),
    ('CSV EXCEL files', '*.csv'),
)


def handel_input(filename, file_extension):
    resultBefore = checkInputFile(filename, file_extension)
    resultAfter = []
    resultAfter.append(['Depth', 'CLI', 'CDO'])
    resultAfter.append(['ft', '%', '%'])
    for x in resultBefore:
        for m in range(10):
            resultAfter.append([x[0]-(9-m), x[1], x[2]])

    return resultAfter


def browseFile():
    # open-file dialog
    filename = filedialog.askopenfilename(
        title='Select a file...',
        filetypes=filetypes,)

    if (filename):
        selectedFilePath.set(filename)
        pathOnly, file_extension = os.path.splitext(filename)
        dataFromFile = handel_input(filename, file_extension)
        if len(dataFromFile) > 2:
            df = DataFrame(dataFromFile)
            df.to_csv('Output_Calcimeter_Converter.csv',
                      index=False, header=False, sep=',')
            messagebox.showinfo(
                'Success', f'File converted successfully')
        else:
            selectedFilePath.set('')
            messagebox.showerror(
                'File error', 'Please load valid calcimeter excel file')
    else:
        selectedFilePath.set('')


def clearFiles():
    cwd = os.getcwd()
    if (os.path.exists(f'{cwd}\Output_Calcimeter_Converter.csv')):
        os.remove(f'{cwd}\Output_Calcimeter_Converter.csv')


clearFiles()

########""" GUI """########

root = Tk()

browseBtn = Button(root, text="Browse File", background='#15133C', foreground='#EC994B', borderwidth=2, relief="raised", padx=5, pady=5,
                   command=browseFile)
browseBtn.place(x=5, y=5, width=100, height=37)

selectedFilePath = StringVar()
currentFilePath = Label(
    root, textvariable=selectedFilePath, background='#15133C', foreground='#EC994B', anchor=W)
currentFilePath.place(x=5, y=50, width=490, height=20)

root.title('Calcimeter_Converter')
root.geometry('500x250')
root.configure(bg='#000')

root.resizable(False, False)
# Setting icon of master window
root.iconbitmap(resource_path('calc_con.ico'))
# Start program
root.mainloop()
