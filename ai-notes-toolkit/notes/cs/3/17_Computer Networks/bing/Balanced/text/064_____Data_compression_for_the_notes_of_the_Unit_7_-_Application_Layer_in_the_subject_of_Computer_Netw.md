### Data compression

Data compression is the process of reducing the amount of data needed for the storage or transmission of a given piece of information, typically by the use of encoding techniques. Data compression can improve the performance and efficiency of computer networks by reducing the time, cost and bandwidth required for data transfer.

There are two main types of data compression techniques: lossless and lossy.

- Lossless compression techniques preserve the exact information of the original data, and allow the original data to be reconstructed from the compressed data without any loss of quality or information. Lossless compression techniques are suitable for text, audio, and some image data that require high fidelity and accuracy.
- Lossy compression techniques discard some information of the original data, and allow the compressed data to be reconstructed with some loss of quality or information. Lossy compression techniques are suitable for image, video, and some audio data that can tolerate some distortion and noise.

Some of the common algorithms used for data compression are:

- Run length encoding (RLE): This technique replaces consecutive identical symbols or bytes with a single symbol or byte followed by the number of repetitions. For example, the string "AAAAABBBBCCCC" can be compressed as "A5B4C4" using RLE. RLE is useful for data sets that contain large amounts of redundant information, such as graphics and video data.
- Differential pulse code modulation (DPCM): This technique encodes the difference between successive samples of a signal, rather than the absolute value of each sample. For example, the sequence "10, 12, 15, 18, 20" can be compressed as "10, 2, 3, 3, 2" using DPCM. DPCM is useful for data sets that have high correlation between adjacent samples, such as audio and image data.
- Dictionary based encoding: This technique uses a predefined dictionary of symbols or strings, and replaces each symbol or string in the data with a code that corresponds to its index in the dictionary. For example, the string "the cat sat on the mat" can be compressed as "1 2 3 4 1 5" using the dictionary {"the", "cat", "sat", "on", "mat"}. Dictionary based encoding is useful for data sets that have high frequency of certain symbols or strings, such as text and image data.