# File Compression-UNIX compress

- File compression is the process of reducing the size of a file by encoding its data more efficiently.
- File compression can save storage space, bandwidth, and transmission time.
- File compression can be lossless or lossy, depending on whether the original data can be perfectly recovered or not.
- UNIX compress is a lossless file compression utility that uses the Lempel-Ziv-Welch (LZW) algorithm.
- The LZW algorithm is based on the idea of building a dictionary of common patterns in the data and replacing them with shorter codes.
- The LZW algorithm works as follows:

  - Initialize the dictionary with 256 entries, corresponding to the 8-bit ASCII characters.
  - Read the next symbol from the input and append it to a string variable S.
  - If S is in the dictionary, go back to step 2.
  - Otherwise, output the code of S without the last symbol, add S to the dictionary with a new code, and set S to the last symbol.
  - Repeat steps 2-4 until the end of the input is reached, then output the code of S.

- The LZW algorithm can achieve high compression ratios for files that contain repetitive patterns or long runs of the same symbol.
- The LZW algorithm can also adapt to different types of data by dynamically updating the dictionary.
- The LZW algorithm has some limitations, such as:

  - The dictionary size is fixed and can be exhausted, leading to reduced compression efficiency or code expansion.
  - The dictionary is not transmitted with the compressed file, so the decompressor must reconstruct it exactly as the compressor did, which can cause errors if the implementations are not compatible.
  - The LZW algorithm is not optimal for compressing files that have high entropy or low redundancy, such as encrypted or random data.