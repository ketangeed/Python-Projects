from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

n = int(input("How many PDFs you want to Merge ?\n"))

for i in range(0, n):
    name = input(f"Enter the name of PDF {i + 1}: ")
    merger.append(name)
    # basically we are taking pdf name as an input from the user...

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()