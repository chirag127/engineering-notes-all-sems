### Diagram Coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Diagram coding is a lossless data compression method that replaces frequently occurring pairs of symbols (digrams) with unused codes.
- Diagram coding works in two passes: the first pass scans the source data and builds a dictionary of digrams and their corresponding codes, the second pass encodes the data using the dictionary .
- Diagram coding can be iterated multiple times, adding more digrams to the dictionary until it is full or the compression ratio is satisfactory.
- Diagram coding can achieve better compression than LZW or BPE for some types of data, such as text or simple images .
- Diagram coding is an example of an ad hoc compression method, meaning that it is not based on a formal model of the source data, but rather on some heuristic or empirical observation .

Here is an example of diagram coding applied to the sentence "This is a test."

- Assume that the source alphabet consists of 26 letters, a space, and a period, and that the unused codes are 28, 29, and 30.
- The first pass scans the source data and finds the following digrams: "is", " a", and "st". These are assigned the codes 28, 29, and 30 respectively, and stored in the dictionary.
- The second pass encodes the data using the dictionary. The encoded data is: 20 8 28 29 1 30 27
- The compression ratio is: (8 * 5) / (7 * 5) = 1.14, meaning that the encoded data is 14% smaller than the original data.