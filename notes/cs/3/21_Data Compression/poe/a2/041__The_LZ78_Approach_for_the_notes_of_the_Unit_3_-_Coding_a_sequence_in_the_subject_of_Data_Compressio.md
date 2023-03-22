 Here is the formal notes in Markdown format on the topic "The LZ78 Approach for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression":

### The LZ78 Approach for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. LZ78 is a dictionary-based compression algorithm. It replaces repeated occurrences of data with references to a dictionary of previously seen data.
2. The dictionary is built dynamically as the input is processed. Each newly encountered string is added to the dictionary.
3. The algorithm encodes each input string by searching the dictionary for the longest prefix match. It then outputs a pointer to the dictionary entry along with the unmatched suffix. The suffix is then added to the dictionary.
4. This approach is superior to LZ77 as it handles overlapping matches and can encode the entire input with just pointer-suffix pairs. However, the decoder must rebuild the entire dictionary, requiring more processing and possibly exceeding the decoder's memory capacity.
5. The key steps in LZ78 are:

a. Start with an empty dictionary
b. Get next input string
c. Search dictionary for longest match
d. Output pointer to match location and unmatched suffix
e. Add unmatched suffix to dictionary
f. Repeat from step b until all input processed

6. Pros: Strong compression, handles overlapping matches.
7. Cons: Decoder requirements can be demanding, dictionary structure can be complex to implement efficiently.

The notes are written in a formal tone with points and without any emojis or external links as per the given instructions. Please let me know if you would like me to modify or expand the notes in any way.