# quantums/Big_Data_Quantum-m.pdf find the text in this file
import os
import subprocess

from PyPDF2 import PdfReader


# ocrmypdf                      # it's a scriptable command line program
#    -l eng+fra                 # it supports multiple languages
#    --rotate-pages             # it can fix pages that are misrotated
#    --deskew                   # it can deskew crooked PDFs!
#    --title "My PDF"           # it can change output metadata
#    --jobs 4                   # it uses multiple cores by default
#    --output-type pdfa         # it produces PDF/A by default
#    input_scanned.pdf          # takes PDF input (or images)
#    output_searchable.pdf      # produces validated PDF output

# ocrmypdf -l eng --rotate-pages --deskew --jobs 8 --output-type pdfa --force-ocr input_scanned.pdf output_searchable.pdf


def main(path="quantums/Big_Data_Quantum-m.pdf"):
    # import the required modules


    if "_ocr" in path:
        return

    # ocr_file_name = "quantums/Big_Data_Quantum-m_ocr.pdf"
    ocr_file_name = path.replace(".pdf", "_ocr.pdf")

    print("ocr_file_name", ocr_file_name)

    # define the path to the folder

    if os.path.exists(ocr_file_name):
        print("file already exist")
        return

    # creating a pdf reader object
    reader = PdfReader(path)

    # printing number of pages in pdf file
    print("total_pages", len(reader.pages))

    total_pages = len(reader.pages)

    all_text = ""

    if total_pages > 5:
        total_pages = 5

    for i in range(total_pages):
        page = reader.pages[i]
        text = page.extract_text()
        all_text += text

    text = all_text

    length = len(text)

    print("length", length)

    length_per_page = length / total_pages

    print("length_per_page", length_per_page)

    if length / total_pages < 200:
        print(
            f"""file need to be scanned with details
filepath : {path}
total_pages : {total_pages}
total_text_length : {length}
length_per_page : {length_per_page}
"""
        )

        subprocess.call(
            [
                "ocrmypdf",
                "-l",
                "eng",
                # "--rotate-pages",
                # "--deskew",
                "--jobs",
                "8",
                "--output-type",
                "pdfa",
                "--force-ocr",
                path,
                ocr_file_name,
            ]
        )

    else:
        print("file is already scanned")

    # ocr_file_name = "quantums/Big_Data_Quantum-m_ocr.pdf"


def try_main(i):
    try:
        main(i)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    import glob

    files = glob.glob("**/*.pdf")

    # import random

    # random.shuffle(files)

    # from concurrent.futures import ProcessPoolExecutor

    # with ProcessPoolExecutor() as executor:
    #     executor.map(main, files)


    # from concurrent.futures import ThreadPoolExecutor

    # with ThreadPoolExecutor() as executor:
    #     executor.map(main, files)

    for i in files:
        main(i)
