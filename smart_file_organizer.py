from pathlib import Path
import shutil

source = Path.home() / "Downloads"

documents = Path.home() / "Documents"

home = documents

# file extensions for organization

file_extensions = {
    ".png": home / "IMAGES",
    ".java": home / "JAVA",
    ".pptx": home / "PPT",
    ".docx": home / "WORD",
    ".jpeg": home / "IMAGES",
    ".jpg": home / "IMAGES",
    ".pdf": home / "PDF",
    ".exe": home / "EXE",
    ".zip": home / "ZIP",
    ".py": home / "PY",
    ".SLDASM": home / "SOLIDWORKS",
    ".SLDDRW": home / "SOLIDWORKS",
    ".SLDPRT": home / "SOLIDWORKS",
    ".doc": home / "WORD",
    ".csv": home / "CSV", 
    ".nc": home / "NC",
    ".mp4": home / "VIDEOS"
}

# move file from source to destination
for file in source.iterdir():
    if file.suffix in file_extensions:

        destination = file_extensions[file.suffix]

        destination.mkdir(parents=True, exist_ok=True) #checks whether destination exists, if not create it

        target_file = destination / file.name
        if not target_file.exists(): #checks if destination has already file
            shutil.move(file, destination)
        else:
            print("File already exists:", file.name)


# # move file from destination to source
# for values in file_extensions.values():
#     if values.exists() and any(values.iterdir()): #check if folder & file exist
#         for file in values.iterdir():
#             shutil.move(file, source)

