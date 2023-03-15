import json
import re
from concurrent.futures import ThreadPoolExecutor
import traceback

import requests

from remove_empty_notes import remove
from utils import (
    create_file,
    generate_message,
    get_acutal_topic_from_topic_with_hash,
    get_all_syllabus_files,
    get_topics_from_ps_file,
    get_valid_file_name,
    is_deepnote,
    myprint,
    write_content_to_file,
)


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

    myprint(response)
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

def write_error_to_file(error):
    if not is_deepnote():

        with open("error.txt", "a+") as error_file:
            error_file.write(f"{error}\n\n")

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
    try:
        data = get_bing_ai_response(message, mode, parentMessageId)
        return data["response"]
    except KeyError:
        write_error_to_file(data + "\n\n")




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


def get_bing_file_path(ps_file, mode, content_type, topic, topic_index):
    """Returns the file path based on the PS file, module, content type, and topic."""
    ps_file_name = ps_file.replace(".txt", "")
    file_name = get_valid_file_name(topic) + ".md"
    file_name = f"{topic_index:03d}_" + file_name
    file_path = f"notes/{ps_file_name}/bing/{mode}/{content_type}/{file_name}"
    return file_path.replace("p_s/", "", 1)


def process_data(
    actual_topic, ps_file, mode, content_type, topic_with_hash, topic_index
):
    """Processes the data returned from the Bing AI API."""

    try:
        file_path = get_bing_file_path(
            ps_file, mode, content_type, topic_with_hash, topic_index
        )

        have_created_file = create_file(file_path)

        if not have_created_file:
            return

        message = generate_message(content_type, topic_with_hash, actual_topic)

        bing_response = get_bing_ai_text_response(message, mode)

        if bing_response:
            write_content_to_file(file_path, bing_response)

            print(f"Successfully wrote content to file: {file_path}")

        else:
            raise Exception("The response from the Bing AI API was empty.")
    except Exception as error:  # pylint: disable=broad-except
        print(f"Failed to write content to file: {file_path}")
        print(error)

        write_error_to_file(error + "\n\n" + file_path + "\n\n")

        traceback.print_exc()



def main():

    remove()


    all_syllabus_files = get_all_syllabus_files()

    all_content_types = ["all", "diagram", "code", "text"]

    all_modes = ["Balanced", "Creative", "Precise"]

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
            actual_topic = get_acutal_topic_from_topic_with_hash(topic)

            for mode in all_modes:
                for content_type in all_content_types:
                    actual_topics.append(actual_topic)
                    ps_files.append(ps_file)
                    modes.append(mode)
                    content_types.append(content_type)

                    topic_with_hashes.append(topic)
                    topic_indexes.append(topic_index)

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(
            process_data,
            actual_topics,
            ps_files,
            modes,
            content_types,
            topic_with_hashes,
            topic_indexes,
        )


if __name__ == "__main__":

    k = 10
    while k > 0:
        try:
            main()
        except Exception as error:
            print(error)
    k -= 1
