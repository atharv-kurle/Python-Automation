# from pathlib import Path
# import fitz
# from reportlab.pdfgen import canvas
# import shutil
# from docx import Document

# pdf_folder = Path.home() / "Documents/PDF"

# all_pdf = []

# # store names & pages in the list
# for pdf in pdf_folder.iterdir():
#     if pdf.suffix == ".pdf":
#         reader = fitz.open(pdf)
#         pdf_info = {
#             "name": pdf.name,
#             "pages": len(reader)
#         }
#         all_pdf.append(pdf_info)

# # store the list data into the csv file
# file = open("pdf_summary.csv", "w")
# file.write("File name,pages\n")

# for pdf in all_pdf:
#     file.write(pdf["name"] + "," + str(pdf["pages"]) + "\n")

# # search for specific keyword from all pdf
# keyword = "Atharv"

# for pdf in pdf_folder.iterdir():
#     reader = fitz.open(pdf)

#     full_text = ""

#     for page in reader:
#         full_text += page.get_text()

#         if keyword in full_text:
#             print(pdf.name)

# # exporting data into the PDF

# all_pdf = []

# pdf = canvas.Canvas("summary.pdf")

# y = 800

# for pdfiter in pdf_folder.iterdir():

#     reader = fitz.open(pdfiter)

#     pdf_info = {
#         "name": pdfiter.name,
#         "pages": len(reader)
#     }

#     all_pdf.append(pdf_info)


# for item in all_pdf:

#     pdf.drawString(50, y, f"{item["name"]} - {item["pages"]} pages")

#     y -= 20

# pdf.save()

# pdf file organization based on its name
# pdf_folder = Path.home() / "Documents/PDF"

# all_keywords = {
#     "Atharv Kurle": pdf_folder / "Resume",
#     "Resume": pdf_folder / "Resume",
#     "Atharv Kurle": pdf_folder / "Resume",
# }

# # move same pdf files into its folders

# for pdf in pdf_folder.iterdir():

#     if pdf.suffix == ".pdf":

#         for keyword, destination in all_keywords.items(): # iterate on all dictonary keywords

#             destination.mkdir(parents=True, exist_ok=True)

#             if keyword in pdf.name:
#                 target_file = destination / pdf.name
#                 if not target_file.exists(): # checks the file already exists at destination
#                     shutil.move(pdf, destination)
#                 else:
#                     print("File already exists:", pdf.name)


# export data into the word

# pdf_folder = Path.home() / "Documents/PDF"

# doc = Document()

# all_pdf = []

# for pdf in pdf_folder.iterdir():

#     if pdf.suffix == ".pdf":

#         reader = fitz.open(pdf)

#         pdf_info = {
#             "name": pdf.name,
#             "pages": len(reader)
#         }

#         all_pdf.append(pdf_info)

# for index, item in enumerate(all_pdf, start=1):

#     doc.add_paragraph(f"{index}. {item["name"]} - {item["pages"]} pages")

# doc.save("summary.docx")


from pathlib import Path
from pypdf import PdfReader
from docx import Document
from reportlab.pdfgen import canvas
import fitz
import shutil

pdf_folder = Path.home() / "Documents/PDF"

folder_names = {
    "Atharv Kurle": pdf_folder / "Resume",
    "Resume": pdf_folder / "Resume",
    "Red meter": pdf_folder / "MSC Meter Reading"
}

for pdf in pdf_folder.iterdir():

    if pdf.suffix == ".pdf":

        for key, destination in folder_names.items():
        
            if key in pdf.name:
                destination.mkdir(parents=True, exist_ok=True)
                target_file = destination / pdf.name
                if not target_file.exists():
                    shutil.move(pdf, destination)
                else:
                    print("File already exist: ", pdf.name)