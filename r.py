# check all the md files in the cwd and subdirectories
import glob
import os


for file in glob.glob("**/*.md", recursive=True):
    # open the file
    with open(file, 'r') as f:
        # read the file
        lines = f.read()

        lines = lines.strip()

        if len(lines.splitlines()) == 1:
            os.remove(file)
