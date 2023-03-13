# check all the folder in the notes folder
import glob
import os
import re


def main():
    a = "notes/*/*/*/*/"
    files = glob.glob(a, recursive=True)

    "notes/poe/1_se/a2/000_#_Software_Engineering.md"

    a = "notes/poe/*/*/"
    files = files + glob.glob(a, recursive=True)


    print(files)
    # return files

    for folder in files:
        if os.path.isdir(folder):
            print(folder)
        else:
            continue

        # check if there are any markdown files in the folder

        files = glob.glob(folder + "/*.md")

        if len(files) == 0:
            continue

        files = glob.glob(folder + "/*.md")

        files = sorted(files, key=lambda x: int(os.path.basename(x).split("_")[0]))

        # allnotes/notes/bing/1_se

        # f = "allnotes/" + folder.replace(folder.split("/")[-1], "") + "/" here the folder is allnotes/notes/bing/1_se/Creative/all/ but we want allnotes/notes/bing/1_se/

        f = "allnotes/" + folder.replace(folder.split("/")[-1], "")


        print(f)

        if not os.path.exists(f):
            os.makedirs(f)

        # f = f + folder.split("/")[-1] + ".md"

        f = f + folder.replace("/", "_") + ".md"

        fi = f

        with open(f, "w", encoding="utf-8") as f:
            f.write("")

        for file in files:
            with open(file, "r", encoding="utf8") as opened_in_read_mode_file:
                content = opened_in_read_mode_file.read()

            if len(re.findall("```", content)) % 2 != 0:
                content = content + "\n\n```\n"


            # check if file have links like ![NameNode high availability diagram](https://i.imgur.com/1Z0qQ2C.png)

            # remove all links from file

            regex = r"!\[(.*?)\]\((.*?)\)"


            # replace all links with the text

            content = re.sub(regex, r"\1", content)

            with open(fi, "a", encoding="utf-8") as opened_in_append_mode_file:
                opened_in_append_mode_file.write("\n\n" + content + "\n\n")


if __name__ == "__main__":
    main()
