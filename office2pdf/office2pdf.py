# coding=utf-8
"""convert file to pdf"""

import win32com as comtypes
import os
import sys
import glob

def ppt2pdf(inputFileName, pdfName):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.visible = 1
    ppt = powerpoint.Presentations.Open(inputFileName)
    ppt.SaveAs(pdfName, 32)
    ppt.close()

def doc2pdf(inputFileName, pdfName):
    word = comtypes.client.CreateObject("Word.Application")
    word.Visible = 0
    doc = word.Documents.Open(inputFileName)
    doc.ExportAsFixedFormat(
        pdfName,
        ExportFormat=17,
        OpenAfterExport=False,
        OptimizeFor=0,
        CreateBookmarks=1)
    doc.close()

def printpdf(inputFileName):
    pdfName = '%s.pdf'%os.path.splitext(inputFileName)[0]
    if os.path.isfile(pdfName):
        return
    ext = os.path.splitext(inputFileName)[1]
    if ext in ('.ppt', '.pptx'):
        ppt2pdf(inputFileName, pdfName)
    elif ext in('.doc', '.docx'):
        doc2pdf(inputFileName, pdfName)

def search_office_file(thePath='.'):
    for walkr in os.walk(thePath):
        for file in walkr[2]:
            if os.path.splitext(file)[1] in ['.ppt', '.pptx', '.doc', ',docx']:
                yield os.path.join(walkr[0], file)

def main():
    for i in search_office_file():
        print(i)
        printpdf(i)

if __name__ == "__main__":
    os.chdir(r'z:\wwg\Library\Docs\_Trans\subjects')
    main()