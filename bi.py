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

def do_content_type_topics(m,j, ps_file, topic, content_type):

    i = topic

    topic = topic.replace("#", "")

    if content_type == "all":

        message = (

            "give a comprehensive overview with definition"

            + f", examples, applications, benefits,types,disadvantes of {topic}"

            + "give Mnemonics or learning tricks for the topic only if there are good Mnemonics or learning tricks respectively, don't give the Mnemonics and learning tricks if not very easy and good Mnemonics and learning tricks are avaliable"

        )

    elif content_type == "text":

        message = f"write in detail about {topic}"

    elif content_type == "image":

        message = f"draw the detailed image for {topic}"

    elif content_type == "diagram":

        message = f"draw comprehensively detailed diagram with details for {topic}"

    elif content_type == "explain":

        message = f"explain in detail about {topic}"

    elif content_type == "ab":

        message = f"what are the applications and benefits of {topic}"

    elif content_type == "ch":

        message = f"provide challenges and solutions of {topic}"

    elif content_type == "code":

        message = f"write code for {topic}"

    elif content_type == "example":

        message = f"provide examples of {topic}"

    elif content_type == "definition":

        message = f"what is the definition of {topic}"

    elif content_type == "vr":

        message = f"give the visual representation for {topic}"

    elif content_type == "summary":

        message = f"what is the summary of {topic}"

    else:

        message = f"tell me in detail about {topic}"

    myprint(message)

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

    file_path = f"notes/bing/{m}/{content_type}/{ps_file.replace('.txt','')}/{file_name}"

    myprint(file_path)

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

        try:

            text = get_bing_ai_res(message,m)

            if not os.path.exists(os.path.dirname(file_path)):

                os.makedirs(os.path.dirname(file_path))

            with open(file_path, "a", encoding="utf8") as file:

                file.write(f"{text}")

        except Exception as e:

            print(e)

            with open("error.txt", "a", encoding="utf8") as file:

                file.write(f"\n\n {e}---" + message)

def get_bing_ai_res(message,m="Balanced"):

    print(message)

# don't write like a chatbot

    message = (

        """don't show feeling with messages like "Hello, this is Bing. I can help you with your question.",

Be formal in your responses.

don't include any emojis in the answer,

write like you are writing the study material to learn and read from for exams so it should be comprehensive and detailed,

don't include any links,

don't include any image links,

write in the markdown format:

"""

        + message

    )

    # if "draw" in message:

    #     m = "Creative"

    # else:

    #     m = "Balanced"

    try:

        response = requests.post(

            "https://bing.khanh.lol/completion",

            timeout=1000,

            headers={"Content-Type": "application/json"},

            # data=json.dumps({"prompt": message,"mode":"Creative"}),

            data=json.dumps({"prompt": message,"mode":m}),

        )

        myprint(response.text)

        data = response.json()

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

            raise

    except Exception as e:

        print(e)

        with open("error.txt", "a", encoding="utf8") as file:

            file.write(f"\n\n{e}-"+message)

            file.write("\n\n\n\n\n\n"+response.text)

def main(content_type="text"):

    files = glob.glob("p_s/**/*.txt",recursive = True)

    print(content_type)

    for m in ["Balanced","Creative","Precise"]:

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

                    do_content_type_topics(m,j, ps_file, topic, content_type)

                    j += 1

            except Exception as e:

                print(e)

                with open("error.txt", "a", encoding="utf8") as file:

                    file.write(f"{e}\n\n")

if __name__ == "__main__":

    def main_1():

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

        ] * 5

        

        import concurrent.futures

        with concurrent.futures.ThreadPoolExecutor(max_workers=len(types)) as executor:

            executor.map(main, types)

    k = 100

    while k > 0:

        try:

            print(k)

            main_1()

            k -= 1

        except Exception as e:

            myprint(e)

            with open("error.txt", "a", encoding="utf8") as file:

                file.write(f"{e}\n\n")

            k -= 1
            
