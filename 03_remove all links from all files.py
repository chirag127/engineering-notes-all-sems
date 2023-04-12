import glob

import os
import re

files = glob.glob("notes/**/*.md", recursive=True)
# notes/2_wt/poe/capybara/002__Introduction_to_Web_Technology.md
print(files)

for file in files:
    if os.path.isfile(file):
        # check if file have links like ![NameNode high availability diagram](https://i.imgur.com/1Z0qQ2C.png)

        regex = r"!\[(.*?)\]\((.*?)\)"

        with open(file, "r", encoding="utf8") as f:
            text = f.read()

        matches = re.findall(regex, text)

        if matches:
            print(file)

            for match in matches:
                print(match)

            print()

            # remove all links from file

            # text = re.sub(regex, r"", text)

            with open(file, "w", encoding="utf8") as f:
                f.write(text)

# Path: remove all links from all files.py
