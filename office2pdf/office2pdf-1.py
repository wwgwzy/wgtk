# coding=utf-8
"""convert file to pdf"""

import comtypes.client, os ,sys
from pathlib import Path

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

def printpdf(inputFileName,lerrordir):
    pdfName = inputFileName.with_suffix('.pdf')
    print pdfName.relative_to(inputFileName.cwd()),
    if pdfName.is_file():
        # print "pdf exists"
        return
    # print "printing...",
    if inputFileName.suffix in ('.ppt', '.pptx'):
        ppt2pdf(str(inputFileName), str(pdfName))
    elif inputFileName.suffix in('.doc', '.docx'):
        doc2pdf(str(inputFileName), str(pdfName))
    # print "pdf printed"


cwd = os.path.split(os.path.realpath(sys.argv[0]))[0]
os.walk(cwd)
os.chdir(cwd)
"""print pdf in */*"""
lerrordir = ''

if __name__ == "__main__":
    for walkr in os.walk(cwd):
        officefiles = [file for file in Path(walkr[0]).glob("*.*") if file.suffix in ('.ppt', '.pptx', '.doc', '.docx' ) and not str(file).startswith('$')]
        for officefile in officefiles:
            try:
                printpdf(officefile, lerrordir)
            except BaseException as e:
                #print e
                nerrordir = str(officefile.parent)
                if lerrordir != nerrordir:
                    lerrordir = nerrordir
                    os.system('start explorer "%s"'%str(officefile.parent))
                wait = raw_input('double press Enter to retry after fix')
                try:
                    printpdf(officefile)
                except:
                    #print "printing fail still, holy shit"