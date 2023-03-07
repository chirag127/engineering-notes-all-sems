import glob
import json
import os
import re

import requests


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
        f"notes/bing/{m}/{content_type}/{ps_file.replace('.txt','')}/{file_name}"
    )

    Actual_topic = Actual_topic.strip()

    topic = Actual_topic

    myprint(file_path)

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    if not os.path.exists(file_path):
        try:
            with open(file_path, "w", encoding="utf8") as file:
                file.write("")

        except Exception as error:
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
        total_reply = ""
        message = f"""- write the content in markdown format.
- Be Formal.
- the content is to be written inside header {i}.
- write on the topic like you are writing the study material to learn and read from for exams.
- write in points.
- you may also include detailed ascii diagrams, codes, markdown tables, advantages, disadvantages, examples, applications, etc for the topic in the reply, only if they can be helpful to learn and read from for exams.
write in detail about {topic}"""

        message = gm + message

        data = get_bing_ai_response(message, m)

        if data["response"]:
            total_reply += data["response"]
            print(total_reply)

            # message = "Include advantages, disadvantes if you think they can be asked in exams."

            # data = get_bing_ai_response(message, m, data["messageId"])

            # if data["response"]:
            #     total_reply = total_reply + "\n\n" + data["response"]

            #     print(total_reply)

            # else:
            #     return

            message = (
                "if there are good Mnemonics and learning tricks for the topic then include them."
                + "don't give the Mnemonics and learning tricks they are not easy to remember."
            )

            data = get_bing_ai_response(message, m, data["messageId"])

            if data["response"]:
                total_reply = total_reply + "\n\n" + data["response"]

                regex = r"\[\^[0-9]+\^\]"

                total_reply = re.sub(regex, "", total_reply)

                total_reply = total_reply.strip()

                with open(file_path, "a", encoding="utf8") as file:
                    file.write(f"{total_reply}")

                return

            else:
                return

        else:
            return

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

    myprint(message)

    message = gm + message

    text = get_bing_ai_res(message, m)

    if text:
        with open(file_path, "a", encoding="utf8") as file:
            file.write(f"{text}")

    else:
        return


def get_bing_ai_response(
    message, m="Balanced", parentMessageId="b4e55ca3-d2a7-46f7-9c2c-d03e192199f2"
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
    myprint(response.text)
    response = response.json()

    return response


def get_bing_ai_res(
    message, m="Balanced", parentMessageId="b4e55ca3-d2a7-46f7-9c2c-d03e192199f2"
):
    print(message)

    # if "draw" in message:
    #     m = "Creative"
    # else:
    #     m = "Balanced"

    data = get_bing_ai_response(message, m, parentMessageId)
    print(data["response"])

    text = data["response"]

    # remove words like [^6^]

    regex = r"\[\^[0-9]+\^\]"

    text = re.sub(regex, "", text)

    text = text.strip()

    # check if the last like of the text contains question mark if it do remove the last line

    if "?" in text.splitlines()[-1]:
        text = text.splitlines()[:-1]
        text = "\n".join(text)

    if text:
        return text

    else:
        return None


def main(content_type="text"):
    files = glob.glob("p_s/**/*.txt", recursive=True)

    print(content_type)

    for m in ["Creative"]:
        # "Balanced",
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
                    do_content_type_topics(m, j, ps_file, topic, content_type)

                    j += 1

            except Exception as e:
                print(e)

                # with open("error.txt", "a", encoding="utf8") as file:
                #     file.write(f"{e}\n\n")


if __name__ == "__main__":

    def main_1():
        from remove_empty_notes import remove

        remove()

        types = [
            "all",
            "diagram",
            "code",
            "text",
        ] * 5

        import concurrent.futures

        # max_workers=len(types)
        # max_workers=

        # with concurrent.futures.ThreadPoolExecutor(max_workers=len(types)) as executor:
        #     executor.map(main, types)
        for type in types:
            main(type)

    k = 100

    while k > 0:
        try:
            print(k)
            main_1()

            k -= 1

        except Exception as e:
            print(e)

            # with open("error.txt", "a", encoding="utf8") as file:
            #     file.write(f"{e}\n\n")

            k -= 1

    # main("all")
