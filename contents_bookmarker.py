#!/usr/bin/env python
from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument('-p', '--pdf_path', type=str, help='Path to the pdf')
parser.add_argument('-o', '--offset', type=int, default=0, help='Difference between content page number and actual page no.')
parser.add_argument('-c', '--contents', type=str, help='Path to the contents text file')
config = parser.parse_args()

filename = config.pdf_path
cont = open(config.contents, 'r', encoding='utf-8')
cont = cont.read()
output = PdfFileWriter()
input1 = PdfFileReader(open(filename, 'rb'))
folder = '/'.join(filename.split('/')[:-1])
os.chdir(folder)

total_page = input1.getNumPages()

for page in range(total_page):
    output.addPage(input1.getPage(page))

plevel = 0
offset = config.offset
stack = []
parent = None
for topics in cont.split('\n')[:-1]:
    topics = topics.strip()
    print(topics, len(topics.split('.')))
    level = len(topics.split('.'))
    l = topics.strip().split(' ')
    print(l)
    page_no = int(l[-1]) + offset
    if level > plevel:
        print('add child bookmark and store parent bookmark')
        stack.append(parent)
        # parent = topics
        parent = output.addBookmark(' '.join((l[0:-1])), page_no, parent=stack[-1])
        plevel = level
    elif level == plevel:
        parent = output.addBookmark(' '.join((l[0:-1])), page_no, parent=stack[-1])
        print('add child bookmark')
    else:
        print('restore parent bookmark and add child bookmark')
        for i in range(plevel - level):
            stack.pop()
        print(plevel - level)
        parent = output.addBookmark(' '.join((l[0:-1])), page_no, parent=stack[-1])
        # stack.append(parent)
        plevel = level
    print(stack, parent) 

with open('[Indexed] '+filename.split('/')[-1] , 'wb') as output_file:
    print('writing file..', '\n', '[Indexed] '+filename.split('/')[-1])
    output.write(output_file)
    print('finished..')
    output_file.close() 
