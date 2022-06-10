import PyInstaller.__main__
import os
import shutil

cwd = os.getcwd()
wd = f'{cwd}\\dist\\Calcimeter_Converter'
if os.path.exists(wd):
    shutil.rmtree(wd)

PyInstaller.__main__.run([
    'Calcimeter_Converter.py',
    # '--onefile',
    '--windowed',
    '--add-data', 'src;src',
    '-i', ".\src\calc_con.ico",
    '--splash', ".\src\calc_con.png",
    '--exclude-module', 'matplotlib',
])
