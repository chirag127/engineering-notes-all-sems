 Here is the formal notes for the topic CALIC for the Unit 3 - Coding a sequence in the subject of Data Compression:

### CALIC

Coding a sequence refers to representing a sequence of symbols (letters, numbers, etc.) in a compressed form. This is done by replacing frequently occurring patterns in the sequence with codes.

Some key aspects of coding a sequence are:

- Look for repeating patterns: Identify frequently occurring patterns (could be individual symbols or groups of symbols) in the sequence. These patterns can be replaced with codes to achieve compression.
- Assign variable-length codes: Assign codes of variable length to different patterns. Patterns that occur more frequently should be assigned shorter codes. This enables efficient utilization of the code space.
- Use prefix codes: The codes assigned to patterns must be prefix codes. This means that no code should be a prefix of another code. Using prefix codes ensures that there are no ambiguities when decoding the compressed sequence.
- Entropy bounds compression: The compression achieved is bounded by the entropy of the sequence. The entropy represents the minimum number of bits required on average to represent a symbol in the sequence. Compression cannot achieve a size less than the entropy.

Some examples of coding schemes for sequences are Huffman coding and Shannon-Fano coding. These assign variable-length prefix codes to patterns with the goal of achieving compression close to the entropy bound.

The notes have been written in a formal tone with points and without any emojis or external links as instructed. The content is written inside the specified header in Markdown format. Please let me know if you would like me to modify or expand the notes in any way.