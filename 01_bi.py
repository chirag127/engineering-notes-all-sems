import glob
import json
import os
import re
from concurrent.futures import ThreadPoolExecutor

import requests


def myprint(text):
    if "work/" not in os.getcwd():
        print(text)


def get_all_syllabus_files():
    files = glob.glob("p_s/**/*.txt", recursive=True)

    files = [file for file in files if "p_s/ps_1.txt" not in file]

    return files


def get_topics_from_ps_file(file):
    with open(file, "r", encoding="utf8") as file:
        message = file.read()
    return message.splitlines()


def get_bing_ai_response(
    message: str,
    mode: str = "Balanced",
    parentMessageId: str = "b4e55ca3-d2a7-46f7-9c2c-d03e192199f2",
) -> str:
    """
    Query the Bing AI API with a message and return the response.

    Parameters:
    message (str): The message to send to the Bing AI API.
    mode (str): The mode to use for the response. Default is "Balanced".
    parentMessageId (str): The ID of the parent message.
    Default is "b4e55ca3-d2a7-46f7-9c2c-d03e192199f2".

    Returns:
    The response from the Bing AI API as a string.
    """
    response = requests.post(
        "https://bing.khanh.lol/completion",
        timeout=1000,
        headers={"Content-Type": "application/json"},
        data=json.dumps(
            {"prompt": message, "mode": mode, "parentMessageId": parentMessageId}
        ),
    )
    response = response.json()
    return response


def remove_reference_word_occurrences(text: str) -> str:
    """
    Remove reference word occurrences from a string.

    Parameters:
    text (str): The string to remove reference word occurrences from.

    Returns:
    The string with reference word occurrences removed.
    """
    regex = r"\[\^[0-9]+\^\]"
    return re.sub(regex, "", text).strip()


def remove_last_line_if_question(text: str) -> str:
    """
    Remove the last line of a string if it ends with a question mark.

    Parameters:
    text (str): The string to remove the last line from if it ends with a question mark.

    Returns:
    The string with the last line removed if it ends with a question mark.
    """
    if "?" in text.splitlines()[-1]:
        text = text.splitlines()[:-1]
        text = "\n".join(text)
    return text


def retrieve_bing_ai_response(message: str, mode: str, parentMessageId: str) -> str:
    """
    Retrieve a response from the Bing AI API.

    Parameters:
    message (str): The message to send to the Bing AI API.
    mode (str): The mode to use for the response.
    parentMessageId (str): The ID of the parent message.

    Returns:
    The response from the Bing AI API as a string.
    """
    data = get_bing_ai_response(message, mode, parentMessageId)
    return data["response"]


def retry_bing_ai_response(
    message: str, mode: str, parentMessageId: str, try_count: int
) -> str:
    """
    Retry getting a response from the Bing AI API.

    Parameters:
    message (str): The message to send to the Bing AI API.
    mode (str): The mode to use for the response.
    parentMessageId (str): The ID of the parent message.
    try_count (int): The number of times to retry getting a response.

    Returns:
    The response from the Bing AI API as a string after retrying.
    """
    print("retrying")

    print(
        f"""
message: {message}
mode: {mode}
parentMessageId: {parentMessageId}
try_count: {try_count}
    """
    )

    return get_bing_ai_text_response(message, mode, parentMessageId, try_count - 1)


def get_bing_ai_text_response(
    message: str,
    mode: str = "Balanced",
    parentMessageId: str = "b4e55ca3-d2a7-46f7-9c2c-d03e192199f2",
    try_count: int = 3,
    topic: str = "",
) -> str:
    """
    Get a response from the Bing AI API with retries.

    Parameters:
    message (str): The message to send to the Bing AI API.
    mode (str): The mode to use for the response. Default is "Balanced".
    parentMessageId (str): The ID of the parent message.
    Default is "b4e55ca3-d2a7-46f7-9c2c-d03e192199f2".
    try_count (int): The number of times to retry getting a response. Default is 3.
    topic (str): The topic of the response. Default is an empty string.

    Returns:
    The response from the Bing AI API as a string.
    """
    if try_count == 0:
        return "tried 3 times\n\n" + "for topic: " + topic + "\n\n"

    text = retrieve_bing_ai_response(message, mode, parentMessageId)
    print(text)

    text = remove_reference_word_occurrences(text)

    if "I am sorry, I am unable to respond" in text:
        return retry_bing_ai_response(message, mode, parentMessageId, try_count - 1)

    text = remove_last_line_if_question(text)

    if text:
        print(text)
        return text
    else:
        print("the text is empty")
        return None


def get_valid_file_name(actual_topic):
    """
    Get a valid file name from the actual topic.

    Parameters:
    actual_topic (str): The actual topic.
    """
    file_name = actual_topic.replace(" ", "_")

    valid_letters_regex = re.compile(r"[^a-zA-Z0-9_-]")

    file_name = valid_letters_regex.sub("_", file_name)

    if len(file_name) > 100:

        file_name = file_name[:100]

    return file_name

def get_acutal_topic_from_file_name(topic):

    acutal_topic = topic.replace("#", "")

    return acutal_topic

def get_bing_file_path(ps_file, mode, content_type, topic,topic_index):
    """Returns the file path based on the PS file, module, content type, and topic."""
    ps_file_name = ps_file.replace('.txt','')
    file_name = get_valid_file_name(topic) + ".md"
    file_name = f"{topic_index:03d}_" + file_name
    file_path = f"notes/{ps_file_name}/bing/{mode}/{content_type}/{file_name}"
    return file_path.replace("p_s/", "", 1)

def create_file(file_path):
    """Creates an empty file at the specified path if it does not exist."""
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    if not os.path.exists(file_path):
        try:
            with open(file_path, "w", encoding="utf8") as file:
                file.write("")

            return True
        except Exception as error: # pylint: disable=broad-except
            print(error)

    return False



def write_content_to_file(file_path, content):
    """Writes the specified content to the file at the specified path."""
    if not os.path.exists(file_path):
        print(f"File does not exist: {file_path}")
        return
    with open(file_path, "a", encoding="utf8") as file:
        file.write(f"{content}")

def generate_message(content_type, topic_with_hash, actual_topic):
    """Generates a message based on the content type and topic."""
    general_message = """- Don't show feeling or friendliness.
- Be formal.
- Don't write any emojis.
- don't inlude the external links. just write or draw everything yourself.
"""
    if content_type == "all":
        message = f"""- write the content in markdown format.
- Be Formal.
- If there are good Mnemonics and learning tricks for the {actual_topic} then include them.
- Don't give the Mnemonics and learning tricks if they are not easy to remember.
- the content is to be written inside header {topic_with_hash}.
- write on the topic like you are writing the study material to learn and read from for exams.
- write in points.
- you may also include detailed ascii diagrams, codes, markdown tables, advantages, disadvantages, examples, applications, etc for the topic in the reply, only if they can be helpful to learn and read from for exams.
the topic to write on is {actual_topic}"""
    elif content_type == "diagram":
        message = f"""- Be Formal.
- the diagram is to be drawn inside header {topic_with_hash}.
- don't give link like ![image caption](https://example.com/image.png), just draw yourself. don't give any links.
- be formal.
- don't give any internet links in the reply although you can use internet to know knowledge on how to draw the diagram in markdown.
- don't include any links or no image links or no urls.
- this is the most important that you don't give any links.
draw detailed ascii diagram for {actual_topic}
"""
    elif content_type == "code":
        message = f"""- write the code to the following question in markdown format.
- Be Formal.
- the content is to be written inside header {topic_with_hash}.
write code for {actual_topic}"""
    else:
        message = f"""- write the content in markdown format.
- Be Formal.
- the content is to be written inside header {topic_with_hash}.
- write on the topic like you are writing the study material to learn and read from for exams.
- write in points.
The topic is {actual_topic}"""
    message = general_message + message
    return message


class data_needed_for_each_request:
    def __init__(self, content_type, filepath, topic_with_hash, actual_topic, mode):
        self.filepath = filepath
        self.topic_with_hash = topic_with_hash
        self.actual_topic = actual_topic
        self.content_type = content_type

def process_data(actual_topic,ps_file, mode, content_type, topic_with_hash,topic_index):
    """Processes the data returned from the Bing AI API."""


    file_path = get_bing_file_path(ps_file, mode, content_type, topic_with_hash,topic_index)

    have_created_file = create_file(file_path)

    if not have_created_file:

        return

    message = generate_message(content_type, topic_with_hash, actual_topic)

    bing_response = get_bing_ai_text_response(message, mode)

    if bing_response:

        write_content_to_file(file_path, bing_response)

        print(f"Successfully wrote content to file: {file_path}")

    else:

        print(f"Failed to write content to file: {file_path}")



def main():

    all_syllabus_files = get_all_syllabus_files()

    all_content_types = ["all", "diagram", "code"]

    all_modes = ["Balanced","Creative","Precise"]

    # actual_topic,ps_file, mode, content_type, topic_with_hash,topic_index

    actual_topics = []
    ps_files = []
    modes = []
    content_types = []

    topic_with_hashes = []
    topic_indexes = []

    for ps_file in all_syllabus_files:

        topics = get_topics_from_ps_file(ps_file)

        for topic_index, topic in enumerate(topics):

            actual_topic = get_acutal_topic_from_file_name(topic)

            for mode in all_modes:

                for content_type in all_content_types:

                    actual_topics.append(actual_topic)
                    ps_files.append(ps_file)
                    modes.append(mode)
                    content_types.append(content_type)

                    topic_with_hashes.append(topic)
                    topic_indexes.append(topic_index)

    with ThreadPoolExecutor(max_workers=20) as executor:

        executor.map(process_data, actual_topics,ps_files, modes, content_types, topic_with_hashes,topic_indexes)

if __name__ == "__main__":

    main()
