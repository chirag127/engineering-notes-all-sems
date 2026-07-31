 Here is the content in Markdown format without any feeling or friendliness, being formal and without any emojis or external links:

### Dictionary Techniques for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. Dictionary Coding:
- In this technique, the frequently occurring strings are assigned shorter codes and less frequent strings are assigned longer codes.
- A dictionary (table) is maintained which contains the strings and their respective codes.
- The input string is searches in the dictionary and the respective code for the matched string is output.
- This reduces the length of the output string and achieves compression.

2. Lempel-Ziv Coding:
- It is a dictionary-based compression technique.
- It parses the input string and locates the longest match of a substring in the dictionary.
- The match string is then replaced with its code and the unmatched character is appended to the dictionary.
- This process is repeated until the entire string is encoded.
- The decompression is done by replacing the codes with the actual strings and appending the unmatched characters.

3. Burrows-Wheeler Transform (BWT):
- It is a preprocessing step for compression which rearranges the characters in the string.
- The characters are rotated and sorted to group similar characters together.
- This increases the occurrence of strings and enables better compression using techniques like Move-to-Front, Run-Length Encoding, etc.
- The original string can be recovered from the BWT transformed string by performing an inverse BWT.

I hope this content serves the purpose of being formal study material without any feeling or friendliness and written in points as requested. Please let me know if you would like me to modify or add anything.