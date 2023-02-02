# get all files in s folder

from concurrent.futures import ThreadPoolExecutor
import os
import random
import time
from revChatGPT.Official import Chatbot


# a = random.randint(1, 1000)
# print("Sleeping for {} seconds".format(a))
# sleep(a)

# Initialize chatbot


def chat(i, file_name) -> bool:

    PROMPT = i

    with open(file_name, "w") as f:

        f.write(PROMPT + "\n")
    print(PROMPT)
    # divide prompt by first space
    PROMPT = PROMPT.split(" ", 1)[1]

    PROMPT = "write in detail about " + PROMPT
    start = time.perf_counter()
    print("User: " + PROMPT)

    api_keys = ["***REMOVED***",
                "***REMOVED***", "***REMOVED***"]

    chatbot = Chatbot(api_key=random.choice(api_keys))

    response = chatbot.ask(PROMPT)
    print("ChatGPT: " + response["choices"][0]["text"])
    end = time.perf_counter()

    print(f"Time taken: {end - start:0.4f} seconds")

    with open(file_name, "w") as f:

        f.write(i + "\n")

        f.write(response["choices"][0]["text"].strip() + "\n")

def main():

    for file in os.listdir("s"):
        if file.endswith(".txt"):
            print(os.path.join("s", file))

        f = "notes/" + file.replace(".txt", "")

        if not os.path.exists(f):
            os.makedirs(f)

        with open("s/" + file, "r") as f:
            s = f.read()

            p = s.splitlines()
            p = [x.strip() for x in p]

            if __name__ == "__main__":
                # Start chat
                a = True
                # a = False

                if a:
                    m = 30
                else:
                    m = 1

                def d(i):
                    PROMPT = i

                    file_name = PROMPT.replace("?", "").replace(" ", "_").replace(
                        "/", "_").replace(":", "_").replace(",", "_").replace("(", "").replace(")", "").replace(".", "").replace('"', '')

                    file_name = str(p.index(i) + 1) + "_" + file_name

                    if len(file_name) > 100:
                        file_name = file_name[:100]

                    file_name = file_name.lower()

                    f = "notes/" + file.replace(".txt", "")

                    file_name = f + "/" + file_name

                    file_name = file_name + ".md"

                    # file_name = "se.md"

                    # check if folder f exists
                    if not os.path.exists(f):
                        os.makedirs(f)

                    if os.path.exists(file_name):
                        print("File already exists")

                        if a:
                            m = 20
                            return
                        else:
                            with open(file_name, "r") as f:
                                lines = f.readlines()

                                if len(lines) > 2:

                                    return
                    chat(PROMPT, file_name)

                with ThreadPoolExecutor(max_workers=m) as executor:
                    executor.map(d, p)

from r import remove

if __name__ == "__main__":

    for i in range(10000):
        remove()
        main()