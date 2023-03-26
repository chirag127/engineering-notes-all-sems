 Here is the content in markdown format without any emojis or external links and in formal tone:

### Basic indexing methods for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

1. B-tree indexing:
- B-tree is a self-balancing data structure that keeps data sorted and allows searches, sequential access, insertions, and deletions all in logarithmic time.
- B-trees are commonly used in databases and filesystems due to their performance on modern storage and memory hardware.
- B-trees keep all keys in sorted order, allowing range queries to be processed efficiently.

2. Hash indexing:
- A hash index uses a hash function to compute an index into an array from each value to be indexed.
- This results in fast lookups, inserts, and deletes as long as the hash function distributes the values evenly.
- However, hash indexes do not support efficient traversal of keys or values in sorted order. They also do not support range queries.

3. Bitmap indexing:
- Bitmap indexing is a space-efficient indexing technique suitable for highly cardinal domains.
- Instead of storing index entries for distinct values as in a B-tree, a bitmap is used with one bit per distinct value.
- Bitmaps allow efficient intersection, union, and difference operations useful for various analytics. However, bitmap indexes are only suitable for low-cardinality domains.

The content covers the key points about the 3 indexing methods in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.