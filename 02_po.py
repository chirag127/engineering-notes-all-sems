"""
sage = capybara
claude = a2
chatgpt = chinchilla
dragonfly = nutria
"""

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
from utils import (
    generate_message,
    get_acutal_topic_from_topic_with_hash,
    get_valid_file_name,
)

set_auth("Quora-Formkey", "2cbcc73d525a277dc9e11ed604bc0c1e")
set_auth("Cookie", "m-b=RwMrxga0QhVonZolW23NIQ==")


def main():
    remove()
    ids = [1, 2, 3, 4]

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(run_bot, ids)

    for idd in ids:
        run_bot(idd)


def run_bot(i):
    files = glob.glob("p_s/**/*.txt", recursive=True)

    files.sort()

    print(files)
    bots = {1: "a2", 2: "capybara", 3: "chinchilla", 4: "nutria"}

    bot = bots[i]
    print("The selected bot is : ", bot)
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
    topic_with_hash="india",
    chat_id=None,
):


    actual_topic = get_acutal_topic_from_topic_with_hash(topic_with_hash)

    print(actual_topic)

    message = generate_message(topic_with_hash, actual_topic)

    file_name = get_file_name(j, actual_topic)

    file_path = f"notes/{file.replace('.txt','')}/poe/{bot}/{file_name}"

    file_path = file_path.replace("p_s/", "", 1)

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf8") as f:
            f.write("")

        clear_context(chat_id)

        send_message(message, bot, chat_id)
        reply = get_latest_message(bot)

        with open(file_path, "a", encoding="utf8") as f:
            f.write(f"{reply}")


def get_file_name(j, actual_topic):

    file_name = f"{get_valid_file_name(actual_topic)}.md"

    file_name = f"{j:03d}_" + file_name

    return file_name


if __name__ == "__main__":
    k = 0
    while k < 100:
        try:

            remove()

            main()
        except Exception as e: # pylint: disable=broad-except
            print(e)
            continue

        k += 1
