import glob
import os
import re


def myprint(text: str = "") -> None:
    """
    Print text if the current working directory is not "work/".

    Parameters:
    text (str): The text to print.
    """
    if not is_deepnote():
        print(text)


def is_deepnote():
    """
    Check if the current working directory is "work/".

    Returns:
    bool: True if the current working directory is "work/", False otherwise.
    """
    return "work/" in os.getcwd()

def get_all_syllabus_files():
    """
    Get all syllabus files.

    Returns:
    list: A list of all syllabus files.
    """
    files = glob.glob("p_s/**/*.txt", recursive=True)

    files.sort()

    files = [file for file in files if "p_s/ps_1.txt" not in file]

    return files


def get_topics_from_ps_file(file):
    """
    Get all topics from a ps file.

    Parameters:
    file (str): The path to the ps file.

    Returns:
    list: A list of all topics.
    """

    with open(file, "r", encoding="utf8") as file:
        message = file.read()
    return message.splitlines()


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


def get_acutal_topic_from_topic_with_hash(topic_with_hash):
    """
    Get the actual topic from the file name.
    """
    acutal_topic = topic_with_hash.replace("#", "")

    return acutal_topic


def create_file(file_path):
    """Creates an empty file at the specified path if it does not exist."""
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    if not os.path.exists(file_path):
        try:
            with open(file_path, "w", encoding="utf8") as file:
                file.write("")

            return True
        except Exception as error:  # pylint: disable=broad-except
            print(error)

    return False


def write_content_to_file(file_path, content):
    """Writes the specified content to the file at the specified path."""
    if not os.path.exists(file_path):
        print(f"File does not exist: {file_path}")
        return
    with open(file_path, "a", encoding="utf8") as file:
        file.write(f"{content}")


def generate_message( topic_with_hash, actual_topic,content_type="text"):
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
