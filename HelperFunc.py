import os
import sys

from HandleExcelFilesType import getCSVData, readXlsFile, readXlsXFile


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, 'src\\', relative_path)


def writeLocalFile(filename, txt):
    f = open(filename, 'w')
    f.write(txt)
    f.close()


def checkInputFile(excelFilename, file_extension):
    if (file_extension == '.csv'):
        return getCSVData(excelFilename)
    elif (file_extension == '.xls'):
        return readXlsFile(excelFilename)
    elif (file_extension == '.xlsx'):
        return readXlsXFile(excelFilename)
    else:
        return []
