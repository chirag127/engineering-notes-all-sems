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

files = ["01_bi.py", "02_po.py", "05_addodd.py"]

with ThreadPoolExecutor() as executor:
    for f in files:
        executor.submit(os.system, f"python {f}")

# for f in files:
#     os.system(f"python {f}")