# # import glob
# # import re


# for file in glob.glob("notes/**/*.md", recursive=True):
#     with open(file, "r", encoding="utf8") as opened_in_read_mode_file:
#         content = opened_in_read_mode_file.read()

#     if len(re.findall("```", content)) % 2 != 0:
#         content = content + "\n\n```\n"

#     with open(file, "w", encoding="utf8") as opened_in_write_mode_file:
#         opened_in_write_mode_file.write(content)
