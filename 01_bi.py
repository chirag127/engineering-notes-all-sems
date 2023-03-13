import glob
import json
import os
import re

import requests
from concurrent.futures import ThreadPoolExecutor


def myprint(message):
    if "work/" in os.getcwd():
        pass
    else:
        print(message)


def do_content_type_topics(m, j, ps_file, topic, content_type):
    i = topic

    topic = topic.replace("#", "")

    Actual_topic = topic

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

    myprint(file_name)

    file_path = (
        f"notes/bing/{ps_file.replace('.txt','')}/{m}/{content_type}/{file_name}"
    )

    # replace the first folder p_s from the path

    file_path = file_path.replace("p_s/", "", 1)

    Actual_topic = Actual_topic.strip()

    topic = Actual_topic

    myprint(file_path)

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    if not os.path.exists(file_path):
        try:
            with open(file_path, "w", encoding="utf8") as file:
                file.write("")

        except Exception as error:  # noqa E722 # pylint: disable=broad-except
            # with open("error.txt", "a", encoding="utf8") as file:
            #     file.write(f"{error}\n\n")

            print(error)

            with open(file_path, "w", encoding="utf8") as file:
                file.write(f"{i}\n\n")

    else:
        return

    gm = """- Don't show feeling or friendliness with "Hello, this is Bing." etc.
- Be formal.
- Don't write any emojis.
- don't inlude the external links. just write or draw everything yourself.
"""

    if content_type == "all":
        message = f"""- write the content in markdown format.
- Be Formal.
- If there are good Mnemonics and learning tricks for the {topic} then include them.
- Don't give the Mnemonics and learning tricks if they are not easy to remember.
- the content is to be written inside header {i}.
- write on the topic like you are writing the study material to learn and read from for exams.
- write in points.
- you may also include detailed ascii diagrams, codes, markdown tables, advantages, disadvantages, examples, applications, etc for the topic in the reply, only if they can be helpful to learn and read from for exams.
the topic to write on is {topic}"""

    elif content_type == "diagram":
        message = f"""- Be Formal.
- the diagram is to be drawn inside header {i}.
- don't say "The following diagram illustrates the basic architecture of a _: and then not give link like ![Map Reduce Architecture](https://www.tutorialspoint.com/map_reduce/images/mapreduce_architecture.jpg)
- be formal.
- don't give any internet links in the reply although you can use internet to know knowledge on how to draw the diagram in markdown.
- don't include any links or no image links or no urls.
- this is the most important that you don't give any links.
draw detailed ascii diagram for {topic}
"""

    elif content_type == "code":
        message = f"""- write the code to the following question in markdown format.
- Be Formal.
- the content is to be written inside header {i}.
write code for {topic}"""
    else:
        message = f"""- write the content in markdown format.
- Be Formal.
- the content is to be written inside header {i}.
- write on the topic like you are writing the study material to learn and read from for exams.
- write in points.
The topic is {topic}"""

    message = gm + message

    text = get_bing_ai_res(message, m, topic=topic)

    if text:
        with open(file_path, "a", encoding="utf8") as file:
            file.write(f"{text}")

    else:
        return


def get_bing_ai_response(
    message,
    m="Balanced",
    parentMessageId="b4e55ca3-d2a7-46f7-9c2c-d03e192199f2",
):
    response = requests.post(
        "https://bing.khanh.lol/completion",
        timeout=1000,
        headers={"Content-Type": "application/json"},
        # data=json.dumps({"prompt": message,"mode":"Creative"}),
        data=json.dumps(
            {"prompt": message, "mode": m, "parentMessageId": parentMessageId}
        ),
    )
    response = response.json()

    return response


def get_bing_ai_res(
    message,
    m="Balanced",
    parentMessageId="b4e55ca3-d2a7-46f7-9c2c-d03e192199f2",
    try_count=3,
    topic="",
):
    # if "draw" in message:
    #     m = "Creative"
    # else:
    #     m = "Balanced"

    if try_count == 0:
        return "tried 3 times\n\n" + "for topic: " + topic + "\n\n"

    data = get_bing_ai_response(message, m, parentMessageId)
    print(data["response"])

    text = data["response"]

    # remove words like [^6^]

    regex = r"\[\^[0-9]+\^\]"

    text = re.sub(regex, "", text)

    text = text.strip()

    if "I am sorry, I am unable to respond" in text:
        print("retrying")

        print(
            f"""
message: {message}
m: {m}
parentMessageId: {parentMessageId}
try_count: {try_count}
"""
        )

        return get_bing_ai_res(message, m, parentMessageId, try_count - 1)

    # check if the last like of the text contains question mark if it do remove the last line

    if "?" in text.splitlines()[-1]:
        text = text.splitlines()[:-1]
        text = "\n".join(text)

    if text:
        return text

    else:
        return None


def main(content_type="text", files=None):
    print(content_type)

    files.sort()

    # files = [file for file in files if "p_s/ps_1.txt" in file]

    def main_2(m):
        def main_3(ps_file):
            try:
                with open(ps_file, "r", encoding="utf8") as file:
                    message = file.read()

                topics = message.splitlines()

                # fo r topic in topics:
                #     do_content_type_topics(m, j, ps_file, topic, content_type)

                #     j += 1

                max_workers = os.cpu_count()
                max_workers = len(topics)
                max_workers = 20

                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    executor.map(
                        do_content_type_topics,
                        [m] * len(topics),
                        range(len(topics)),
                        [ps_file] * len(topics),
                        topics,
                        [content_type] * len(topics),
                    )

            except Exception as e:  # pylint: disable=broad-except
                print(e)

                # with open("error.txt", "a", encoding="utf8") as file:
                #     file.write(f"{e}\n\n")

        max_workers = os.cpu_count()
        max_workers = len(files)

        max_workers = 6

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(main_3, files)

    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     executor.map(main_2, [ "Creative"])
    main_2("Creative")


# , "Precise"


if __name__ == "__main__":

    def main_1(files=None):
        from remove_empty_notes import remove

        remove()

        types = [
            "all",
            "diagram",
            "text",
        ]

        max_workers = os.cpu_count()
        max_workers = len(types)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(main, types, [files] * len(types))

    k = 100

    while k > 0:
        try:
            print(k)
            files = glob.glob("p_s/*.txt")

            main_1(files)

            k -= 1

        except Exception as e:  # pylint: disable=broad-except
            myprint(e)

            k -= 1

    k = 100

    while k > 0:
        try:
            print(k)

            files = glob.glob("p_s/**/*.txt", recursive=True)

            main_1(files)

            k -= 1

        except Exception as e:
            myprint(e)

            k -= 1
