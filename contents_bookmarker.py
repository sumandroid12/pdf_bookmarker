from PyPDF2 import  PdfFileReader, PdfFileWriter

filename = '/home/suman/code/python/bookmark_pdf/Douglas C.- Computer Architecture.pdf'
cont = open('contents', 'r', encoding='utf-8')
cont = cont.read()
output = PdfFileWriter()
input1 = PdfFileReader(open(filename, 'rb'))
total_page = input1.getNumPages()

for page in range(total_page):
    output.addPage(input1.getPage(page))

plevel = 0
offset = 24
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

with open('Indexed '+filename.split('/')[-1] , 'wb') as output_file:
    print('finished..')
    output.write(output_file)
    output_file.close() 