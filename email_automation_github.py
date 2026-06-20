import smtplib
from email.message import EmailMessage
from pathlib import Path
import fitz

# connect to the gmail to smtp server
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

# email & app password login
server.login("put_your_email", "app_password")

# get the local pdf folder
pdf_folder = Path.home() /"Documents/PDF"

all_pdf = []

# extract the pdf name, pages length & store in the list
for pdf in pdf_folder.iterdir():
    if pdf.suffix == ".pdf":
        reader = fitz.open(pdf)

        pdf_info = {
            "name": pdf.name,
            "pages": len(reader)
        }

        all_pdf.append(pdf_info)

# create the new csv file
file = open("pdf_summary2.csv", "w")
file.write("File name,Pages\n")

# list -> csv
for pdf in all_pdf:
    file.write(f"{pdf["name"]}, {pdf["pages"]}\n")

file.close()

# extract csv data
with open("C:/Users/Shree/Desktop/PYTHON/pdf_summary2.csv", "rb") as file:
    data = file.read()

recipients = []

# extract emails to send
with open("C:/Users/Shree/Desktop/PYTHON/AUTOMATION PROJECT/email.txt") as file:
    for line in file:
        recipients.append(line.strip())

sender = "put_your_email"

# send the receivers
for receiver in recipients:
    email = EmailMessage()
    email["From"] = sender
    email["To"] = receiver
    email["Subject"] = "Test"
    email.set_content("Hi i am ATHARV")

    email.add_attachment(
        data,
        maintype="text",
        subtype="csv",
        filename="pdf_summary2.csv",
    )

    server.send_message(email)

server.quit()


