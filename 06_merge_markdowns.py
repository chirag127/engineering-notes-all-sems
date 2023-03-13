# check all the folder in the notes folder
import glob
import os


def main():
    a = "notes/**"
    for folder in glob.glob(a, recursive=True):
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

        # f = "allnotes/" + folder.replace(folder.split("/")[-1], "")

        f = "allnotes/" + folder.replace(folder.split("/")[-1], "") + "/"

        print(f)

        if not os.path.exists(f):
            os.makedirs(f)

        # f = f + folder.split("/")[-1] + ".md"

        f = f + folder.replace("/", "_") + ".md"

        fi = f

        with open(f, "w",encoding="utf-8") as f:
            f.write("")

        for file in files:
            with open(file, "r",encoding="utf-8") as f:
                content = f.read()

            with open(fi, "a",encoding="utf-8") as f:
                f.write( "\n\n" + content + "\n\n")



if __name__ == "__main__":
    main()
