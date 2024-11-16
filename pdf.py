import PyPDF2
import sys

inputs = sys.argv[1:]


def add_watermark(pdf_file):
    reader = PyPDF2.PdfFileReader(pdf_file)
    writer = PyPDF2.PdfFileWriter()
    for index in list(range(0, len(reader.pages))):
        content = reader.pages[index]
        mediabox = content.mediaBox
        watermark = PyPDF2.PdfFileReader('wtr.pdf')
        image_page = watermark.pages[0]
        image_page.mergePage(content)
        image_page.mediaBox = mediabox
        writer.addPage(image_page)
        with open('super_wtr.pdf', 'wb') as new_file:
            writer.write(new_file)


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')


def rotate_pdf():
    with open('dummy.pdf', 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        page = reader.getPage(0)
        page.rotateCounterClockwise(90)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open('tilt.pdf', 'wb') as new_file:
            writer.write(new_file)


if __name__ == '__main__':
    # rotate_pdf()
    # pdf_combiner(inputs)
    add_watermark('twopage.pdf')
