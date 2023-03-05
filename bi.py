import glob
import json
import os
import re

import requests


def do_content_type_topics(j,ps_file, topic, content_type):
    i = topic

    topic = topic.replace("#", "")
    if content_type == "all":
        message = (
            "give a comprehensive overview with definitions"
            + f", examples, applications, benefits of {topic}"
            + "  with definitions, examples, applications"
            + " , benefits for Unit 1 - Introduction to Big Data."
        )

    elif content_type == "text":
        message = f"write in detail about {topic}"

    elif content_type == "image":
        message = f"draw, give and show detailed image for {topic}"
    elif content_type == "diagram":
        message = f"draw and show me comprehensively detailed diagram with details for {topic}"

    elif content_type == "explain":
        message = f"explain in detail about {topic}"

    elif content_type == "ab":
        message = f"what are the applications and benefits of {topic}"

    elif content_type == "ch":
        message = f"provide challenges and solutions of {topic}"

    elif content_type == "code":
        message = f"write code for {topic}"

    elif content_type == "example":
        message = f"provide examples for {topic}"

    elif content_type == "definition":
        message = f"what is the definition of {topic}"

    elif content_type == "vr":
        message = f"give the visual representation for {topic}"

    elif content_type == "summary":
        message = f"what is the summary for {topic}"

    else:
        message = f"tell me in detail about {topic}"

    print(message)

    if len(topic) > 100:
        topic = topic[:100]

    topic = topic.replace(" ", "_")

    topic = topic.replace("/", "_")

    topic = topic.replace(":", "_")

    topic = topic.replace("?", "_")

    topic = topic.replace("!", "_")

    topic = topic.replace(",", "_")

    topic = topic.replace(".", "_")

    topic = topic.replace("(", "_")

    topic = topic.replace(")", "_")

    file_name = f"{topic}.md"



    file_name = f"{j:03d}_" + file_name

    print(file_name)

    file_path = f"notes/bing/{content_type}/{ps_file.replace('.txt','')}/{file_name}"

    print(file_path)

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    if not os.path.exists(file_path):
        try:
            with open(file_path, "w", encoding="utf8") as file:
                file.write(f"{i.split('for the notes')[0]}\n\n")

        except Exception as error:
            with open("error.txt", "a", encoding="utf8") as file:
                file.write(f"{error}\n\n")

            with open(file_path, "w", encoding="utf8") as file:
                file.write(f"{i}\n\n")

        response = requests.post(
            "https://bing.khanh.lol/completion",
            timeout=60,
            headers={"Content-Type": "application/json"},
            data=json.dumps({"prompt": message}),
        )

        data = response.json()
        print(data["response"])

        text = data["response"]
        print(text)

        # remove words like [^6^]

        regex = r"\[\^[0-9]+\^\]"

        text = re.sub(regex, "", text)

        text = text.strip()

        # check if the last like of the text contains question mark if it do remove the last line

        if "?" in text.splitlines()[-1]:
            text = text.splitlines()[:-1]
            text = "\n".join(text)

        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        with open(file_path, "a", encoding="utf8") as file:
            file.write(f"{text}")


def main(content_type="text"):
    files = glob.glob("p_s/**.txt")

    for _ in [2, 1, 3]:
        for ps_file in files:
            try:
                with open(ps_file, "r", encoding="utf8") as file:
                    message = file.read()

                topics = message.splitlines()

                # for topic in topics:

                # with ThreadPoolExecutor(max_workers=2) as executor:
                #     executor.map(do_content_type_topics, topics)

                j = 0

                for topic in topics:
                    do_content_type_topics(j ,ps_file, topic, content_type)

                    j += 1

            except Exception as e:
                print(e)

                with open("error.txt", "a", encoding="utf8") as file:
                    file.write(f"{e}\n\n")


if __name__ == "__main__":
    from remove_empty_notes import remove

    remove()

    types = [
        "all",
        "text",
        "image",
        "diagram",
        "explain",
        "ab",
        "ch",
        "code",
        "example",
        "definition",
        "vr",
        "summary",
    ]

    k = 1000

    import concurrent.futures

    while k > 0:
        k -= 1

        with concurrent.futures.ThreadPoolExecutor(max_workers=len(types)) as executor:
            executor.map(main, types)
