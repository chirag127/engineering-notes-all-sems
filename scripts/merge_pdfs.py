"""get all the folders in the current directory and
the subdirectories and merge all the pdfs in that directory into one pdf
if there are no pdfs in the directory, then skip it
"""

import glob
import os
import PyPDF2


def merge_pdfs(parent_dir,out_full_path):
    """merge all the pdfs in the current directory of the pdf
     merge all the pdfs in that directory into one pdf
    if there are no pdfs in the directory, then skip it, the name of
    the output file is the name of the directory + _alll_in_one.pdf
    """

    if not os.path.exists(out_full_path):


        if  os.path.exists(os.path.join(parent_dir, "large.txt")):
            print("large.txt exists, so we will not merge the pdfs")
            return

        a = os.path.join(parent_dir, '**/*.pdf')


        print(a)

        pdfs = glob.glob(a, recursive=True)

        print(pdfs)

        # sort the pdfs by name
        pdfs.sort()



        print(pdfs)

        merger = PyPDF2.PdfMerger()

        for pdf in pdfs:

            print(pdf)

            try:

                # don't merge the output file with the other pdfs if
                # the output size is larger than 50 MB

                if os.path.getsize(pdf) > 50000000 or "_in_one.pdf" in pdf:
                    print("output file is too large, so we will not merge the pdfs")

                    continue



                merger.append(pdf)

            except Exception as error: # pylint: disable=broad-except

                print(error)
                print("error with", pdf)


        merger.write(out_full_path)


    # check if the output file is larger than 90 MB
    # if it is, then delete it
    # if it is not, then keep it
    if os.path.getsize(out_full_path) > 90000000:
        os.remove(out_full_path)
        print("deleted", out_full_path)


        with open(os.path.join(parent_dir, "large.txt"), "w") as file:
            file.write("The following files are too large to be merged into one pdf file: \n")
            for pdf in pdfs:
                file.write(pdf + "is of size" + str(os.path.getsize(pdf)) + "\n")




    else:
        print("kept", out_full_path)


def main():
    """get all the folders in the current directory and
    the subdirectories and merge all the pdfs in that directory into one pdf
    if there are no pdfs in the directory, then skip it
    """

    all_pdfs = glob.glob("**/*.pdf", recursive=True)


    folders = []

    for pdf_file in all_pdfs:

        print(pdf_file)


        # get the full parent directory path

        parent_dir = os.path.dirname(pdf_file)

        folders.append(parent_dir)


    folders = list(set(folders))

    print(folders)

    for parent_dir in folders:

        print(parent_dir)

        old_out_full_path = os.path.join(parent_dir, os.path.basename(parent_dir) + "_alll_in_one.pdf")

        new_out_full_path = os.path.join(parent_dir,parent_dir.replace("/","_") + "_alll_in_one.pdf")

        if os.path.exists(old_out_full_path):
            os.rename(old_out_full_path, new_out_full_path)

        out_full_path = new_out_full_path


        merge_pdfs(parent_dir,out_full_path)

if __name__ == "__main__":
    main()
