# get all files in s folder

from concurrent.futures import ThreadPoolExecutor
import os
import random
import time
from revChatGPT.Official import Chatbot

from r import remove

# a = random.randint(1, 1000)
# print("Sleeping for {} seconds".format(a))
# sleep(a)

# Initialize chatbot


api_keys = [
    "***REMOVED***",
    "***REMOVED***",
    "***REMOVED***",
]

chatbot = Chatbot(api_key=random.choice(api_keys))


def chat(i, file_name) -> bool:
    PROMPT = i

    with open(file_name, "w") as f:
        f.write(PROMPT + "\n")
    print(PROMPT)

    try:
        # divide prompt by first space
        PROMPT = PROMPT.split(" ", 1)[1]
    except Exception as error:
        print("No space in prompt")
        print(error)

    PROMPT = "write in detail about " + PROMPT


    try:
        start = time.perf_counter()
        print("User: " + PROMPT)

        response = chatbot.ask(PROMPT)
        print("ChatGPT: " + response["choices"][0]["text"])
        end = time.perf_counter()

        print(f"Time taken: {end - start:0.4f} seconds")
    except Exception as error:
        print("Error: " + str(error))
        return False
        

    with open(file_name, "w") as f:
        f.write(i)

        f.write("\n\n" + response["choices"][0]["text"].strip() + "\n")


def main(files):
    for file in files:
        if file.endswith(".txt"):
            process_file_name = file
            file = file.replace("p_s/", "")

        f = "notes/" + file.replace(".txt", "")

        if not os.path.exists(f):
            os.makedirs(f)

        notes_folder = f

        with open(process_file_name, "r") as f:
            s = f.read()

            p = s.splitlines()
            p = [x.strip() for x in p]

            if __name__ == "__main__":
                # Start chat
                a = True
                # a = False

                if a:
                    m = 10
                else:
                    m = 1

                def d(i):
                    PROMPT = i

                    file_name = (
                        PROMPT.replace("?", "")
                        .replace(" ", "_")
                        .replace("/", "_")
                        .replace(":", "_")
                        .replace(",", "_")
                        .replace("(", "")
                        .replace(")", "")
                        .replace(".", "")
                        .replace('"', "")
                    )

                    file_name = str(p.index(i) + 1) + "_" + file_name

                    if len(file_name) > 100:
                        file_name = file_name[:100]

                    file_name = file_name.lower()

                    file_name = notes_folder + "/" + file_name

                    file_name = file_name + ".md"

                    # check if folder f exists
                    if not os.path.exists(notes_folder):
                        os.makedirs(notes_folder)

                    if os.path.exists(file_name):
                        print("File already exists")

                        if a:
                            return
                        else:
                            with open(file_name, "r") as f:
                                lines = f.readlines()

                                if len(lines) > 1:
                                    return
                    chat(PROMPT, file_name)

                with ThreadPoolExecutor(max_workers=m) as executor:
                    executor.map(d, p)

                # for i in p:
                #     d(i)



if __name__ == "__main__":
    import glob

    for i in range(1):
        # get all files in p_s folder
        files = glob.glob("p_s/**/*.txt", recursive=True)

        # remove files in notes folder
        remove()

        main(files)
