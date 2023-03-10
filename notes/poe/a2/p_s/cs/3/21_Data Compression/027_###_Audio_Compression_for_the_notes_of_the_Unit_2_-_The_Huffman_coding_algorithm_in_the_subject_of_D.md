 Here is the content in markdown format for the given topic:

### Audio Compression

Audio compression is a form of data compression designed specifically for digital audio signals. The goal is to reduce the amount of data needed to represent the audio signal, allowing for more efficient storage and transmission of the audio.

For the notes of Unit 2 - The Huffman coding algorithm, we will discuss the following points regarding audio compression:

1. Audio compression algorithms - The most common audio compression algorithms are:
- MP3 - Uses perceptual coding techniques to greatly reduce the amount of data needed to represent audio. MP3 is a lossy compression format.
- AAC - Similar to MP3 but more efficient. Also uses perceptual coding and is a lossy format.
- FLAC - A lossless compression format, meaning the original audio signal can be perfectly reconstructed from the compressed data. However, the compression ratios are lower than lossy formats.
- OGG Vorbis - An open source, lossy audio compression format.

2. How audio compression works - Audio compression algorithms take advantage of aspects of human perception to reduce the amount of data needed to represent audio. Some of the key techniques used are:
- Removing inaudible frequencies - Frequencies above 20 kHz are removed since humans can't perceive them.
- Perceptual coding - The algorithm determines which frequencies and sounds are less important to human perception and allocates fewer bits to represent them.
- Masking - The algorithm determines which frequencies are masked by louder frequencies and allocates fewer bits to the masked frequencies.

[Additional points and examples can be added here]

The key advantages of audio compression are reducing storage space and transmission bandwidth requirements. This allows for efficient storage of audio on devices with limited storage like smartphones as well as efficient streaming of audio over networks. The disadvantages are that compression can result in loss of audio quality and the process of compression/decompression requires computational resources.