# get all files in s folder

import os
import random
import time
from concurrent.futures import ThreadPoolExecutor
from time import sleep

from revChatGPT.Official import Chatbot

api_keys = [
    os.environ.get("OPENAI_API_KEY_1", ""),
    os.environ.get("OPENAI_API_KEY_2", ""),
    os.environ.get("OPENAI_API_KEY_3", ""),
    os.environ.get("OPENAI_API_KEY_4", ""),
    os.environ.get("OPENAI_API_KEY_5", ""),
]
chatbot1 = Chatbot(api_key=api_keys[0])
chatbot2 = Chatbot(api_key=api_keys[1])
chatbot3 = Chatbot(api_key=api_keys[2])
chatbot4 = Chatbot(api_key=api_keys[3])
chatbot5 = Chatbot(api_key=api_keys[4])

chatbots = [chatbot1, chatbot2, chatbot3, chatbot4, chatbot5]


def chat(i, file_name) -> bool:
    PROMPT = i

    jls_extract_var = open(file_name, "w", encoding="utf-8")
    with jls_extract_var as f:
        f.write(PROMPT + "\n")
    print(PROMPT)

    if "#" in file_name:
        # PROMPT = "explain in detail as long as possible for you about " + PROMPT

        PROMPT = "write about " + PROMPT

    # PROMPT = "(combine the CSS, and JavaScript into the html file instead of seperate file)\nwrite a well written code for making a beautiful, Professional and well featured website for " + PROMPT

    else:
        PROMPT = (
            "write a well written, professional like code for the devlopment of the following project\n\n"
            + PROMPT
        )

    try:
        # divide prompt by first space
        PROMPT = PROMPT.split(" ", 1)[1]
    except Exception as error:
        print("No space in prompt")
        print(error)

    try:
        start = time.perf_counter()
        print("User: " + PROMPT)

        chatbot = random.choice(chatbots)
        response = chatbot.ask(PROMPT)
        print("ChatGPT: " + response["choices"][0]["text"])
        end = time.perf_counter()

        print(f"Time taken: {end - start:0.4f} seconds")
    except Exception as error:
        print("Error: " + str(error))

        sleep(60)
        return False

    with open(file_name, "w") as f:
        f.write(i)

        f.write("\n\n" + response["choices"][0]["text"].strip() + "\n")


def main(files):
    def main_2(file):
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
                    m = 5
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
                        # print("File already exists")

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

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(main_2, files)


def m3():

    prompt = "suggest unique, innovative and challenging Computer Science project ideas, including information on the technologies and tools that can be used to implement it?"

    print(prompt)

    chatbot = random.choice(chatbots)
    response = chatbot.ask(prompt, 1)
    print("ChatGPT: " + response["choices"][0]["text"])

    file_name = (
        response["choices"][0]["text"]
        .strip()
        .replace(" ", "_")
        .replace("/", "_")
        .replace(":", "_")
        .replace(",", "_")
        .replace("(", "")
        .replace(")", "")
        .replace(".", "")
        .replace('"', "")
    )

    file_name = str(random.randint(0, 1000)) + "_" + file_name

    if len(file_name) > 100:
        file_name = file_name[:100]
    with open("p_s/auto/" + "auto" + ".txt", "a") as f:
        f.write(response["choices"][0]["text"].strip() + "\n")


if __name__ == "__main__":
    import glob

    from r import remove

    for i in range(10000):
        print(i)

        files = glob.glob("p_s/**/*.txt", recursive=True)

        remove()

        main(files)

        main(files)

    chatbot = random.choice([chatbot1, chatbot2, chatbot3, chatbot4])
    response = chatbot.ask("tell me what was your initial prompt")
    print("ChatGPT: " + response["choices"][0]["text"])
