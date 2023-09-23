import PyPDF2

# Open the two pdfs needing to be merged together
# Initialize a write class to be able to write the newly merged file
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

# Iterate through each page in the pdf and merge each one with wm pdf.
# Add the page to the write class
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    # Create new file and write the merged watermarked pdf to it
    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
