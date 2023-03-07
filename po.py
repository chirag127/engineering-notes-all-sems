import glob
import os
from concurrent.futures import ThreadPoolExecutor

from POE import (
    clear_context,
    get_latest_message,
    load_chat_id_map,
    send_message,
    set_auth,
)
from remove_empty_notes import remove

set_auth("Quora-Formkey", "2cbcc73d525a277dc9e11ed604bc0c1e")
set_auth("Cookie", "m-b=RwMrxga0QhVonZolW23NIQ==")

# sage = capybara
# claude = a2
# chatgpt = chinchilla
# dragonfly = nutria


def main():
    remove()
    ids = [1, 2, 3, 4]

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(run_bot, ids)

    for id in ids:
        run_bot(id)


def run_bot(i):
    files = glob.glob("p_s/cs/3/*.txt")

    bots = {1: "a2", 2: "capybara", 3: "chinchilla", 4: "nutria"}

    bot = bots[i]
    print("The selected bot is : ", bot)
    # ---------------------------------------------------------------------------
    chat_id = load_chat_id_map(bot)
    clear_context(chat_id)
    print("Context is now cleared")

    for file in files:
        with open(file, "r", encoding="utf8") as f:
            message = f.read()

        topics = message.splitlines()
        j = 0

        for topic in topics:
            write_a_topic(bot, file, j, topic, chat_id)

            j += 1


def write_a_topic(
    bot="a2",
    file="p_s/cs/3/1_Software Engineering.txt",
    j=0,
    topic="india",
    chat_id=None,
):
    i = topic

    actual_topic = topic.replace("#", "").strip()

    print(actual_topic)

    message = f"""- write the content in markdown format.
- Be Formal.
- the content is to be written inside header {i}.
- write on the topic like you are writing the study material to learn and read from for exams.
- write in points.
- you may also include detailed ascii diagrams, codes, markdown tables, advantages, disadvantages, examples, applications, etc for the topic in the reply, only if they can be helpful to learn and read from for exams.
write in detail about {topic}"""

    file_name = get_file_name(j, topic)

    print(message)

    # file_path = f"notes/poe/p_s/cs/3/1_Software Engineering/{file_name}"

    file_path = f"notes/poe/{bot}/{file.replace('.txt','')}/{file_name}"

    print(file_path)

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf8") as f:
            f.write("")

        clear_context(chat_id)

        send_message(message, bot, chat_id)
        reply = get_latest_message(bot)
        print(f"{bot} : {reply}")

        with open(file_path, "a", encoding="utf8") as f:
            f.write(f"{reply}")


def get_file_name(j, topic):
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

    # add number to filename like 001 002 003 004 005 006 007 008 009 010

    file_name = f"{j:03d}_" + file_name

    print(file_name)
    return file_name


if __name__ == "__main__":
    k = 0
    while k < 1000:
        try:
            from remove_empty_notes import remove

            remove()

            main()
        except Exception as e:
            print(e)
            continue

        k += 1
