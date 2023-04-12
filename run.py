"""Run all the python files in the folder concurrently"""

import os
import glob
from concurrent.futures import ThreadPoolExecutor

# get all the python files in the folder
files = glob.glob("*.py")

# remove this file from the list
files.remove("run.py")

# remove the files that start with _
files = [f for f in files if not f.startswith("_")]

# sort the files
files.sort()


# # run all the files concurrently

# files = ["01_bi.py", "02_po.py"]

# with ThreadPoolExecutor() as executor:
#     for f in files:
#         executor.submit(os.system, f"python {f}")

# for f in files:
# #     os.system(f"python {f}")
# 01_bi.py
# 02_po.py
# 03_remove all links from all files.py
# 05_addodd.py
# 06_merge_markdowns.py
# 07_convert_all_markdown_to_pdf.py
# 16_pdf_ocr.py

# os.system("python 01_bi.py")
# os.system("python 02_po.py")

def os_system(command):
    os.system(command)


os_system('python "03_remove all links from all files.py"')
os_system("python 05_addodd.py")
os_system("python 06_merge_markdowns.py")
os_system("python 07_convert_all_markdown_to_pdf.py")
os_system("python 16_pdf_ocr.py")
