import glob
import os

import subprocess

from concurrent.futures import ThreadPoolExecutor

# convert all files in allnotes to pdf to allnotes/notes/pdf/

files = glob.glob("allnotes/notes/**/*.md", recursive=True)


def main(file):
    pdf_file_path = "allnotes/pdf/" + os.path.basename(file).replace(".md", ".pdf")



    # check if directory exists
    pdf_dir = os.path.dirname(pdf_file_path)
    if not os.path.exists(pdf_dir):
        print("Creating directory " + pdf_dir)
        os.makedirs(pdf_dir)

    print("Checking if " + pdf_file_path + " exists")

    if not os.path.exists(pdf_file_path):
        print("Converting " + file + " to pdf")
        subprocess.call(
            [
                "pandoc",
                file,
                "--pdf-engine=xelatex","-o",

                pdf_file_path,
            ]
        )

        # pypandoc.convert_file(file, "pdf", outputfile=pdf_file_path)


# with ThreadPoolExecutor(max_workers=4) as executor:
#     executor.map(main, files)

for file in files:
    main(file)