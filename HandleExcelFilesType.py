import xlrd
import openpyxl


def readLocalFile(filename):
    f = open(filename, 'r')
    txt = f.read()
    f.close()

    return txt


def readXlsXFile(excelFilename):
    workbook = openpyxl.load_workbook(excelFilename, data_only=True)

    worksheet = workbook.active

    all_rows = []
    try:
        for idx, row in enumerate(worksheet):
            if idx > 0:
                current_row = []
                for cell in row:
                    current_row.append(int(cell.value))
                all_rows.append(current_row)
    except ValueError:
        all_rows = []

    return all_rows


def readXlsFile(excelFilename):
    workbook = xlrd.open_workbook(excelFilename)
    sh = workbook.sheet_by_index(workbook.nsheets-1)

    finalValues = []
    try:
        for rx in range(sh.nrows):
            if rx > 0:
                finalValues.append([int(i) for i in sh.row_values(rx)])
    except ValueError:
        finalValues = []

    return finalValues


def getCSVData(excelFilename):
    resultBefore = []

    text = readLocalFile(excelFilename)
    try:
        for idx, line in enumerate(text.splitlines()):
            if idx > 0:
                resultBefore.append([int(i) for i in line.split(",")])
    except ValueError:
        resultBefore = []

    return resultBefore
