# check all the folder in the notes folder
import glob
import os

sem = "2"


def main(sem):
    for folder in glob.glob(f"notes/cs/{sem}/*"):
        if os.path.isdir(folder):
            print(folder)

        files = glob.glob(folder + "/*.md")

        files = sorted(files, key=lambda x: int(x.split("_")[0].split("/")[-1]))

        f = f"allnotes/cs/{sem}"

        if not os.path.exists(f):
            os.makedirs(f)

        f = f + "/" + folder.split("/")[-1] + ".md"

        fi = f

        with open(f, "w") as f:
            f.write("")

        for file in files:
            with open(file, "r") as f:
                content = f.read()

            with open(fi, "a") as f:
                f.write(content)


for i in range(1, 5):
    main(str(i))
