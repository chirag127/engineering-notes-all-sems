# Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation. It can reduce the storage space and transmission time of data. 
- Coding a sequence is a technique of data compression that assigns codes to sequences of bytes or symbols, rather than individual ones. It can exploit the repetition and correlation in the data to achieve higher compression ratios.  
- Some applications of coding a sequence are:

  - **LZW (Lempel–Ziv–Welch) compression**: This is a lossless compression algorithm that uses a dictionary of codes to represent sequences of bytes. It is widely used in GIF images, Unix compress, and ZIP files.  
  - **Huffman coding**: This is a lossless compression algorithm that uses variable-length codes to represent symbols based on their frequencies. It is optimal for compressing data with known or fixed probabilities. It is used in JPEG images, MP3 audio, and DEFLATE compression. 
  - **Arithmetic coding**: This is a lossless compression algorithm that uses fractional codes to represent symbols based on their probabilities. It can achieve higher compression ratios than Huffman coding, but it is more complex and slower. It is used in JPEG 2000 images, Bzip2 files, and H.264 video. 
  - **Sequence statistical code**: This is a lossless compression algorithm that uses SDC and FOST codes to represent sequences of bytes based on their statistics. It is designed to improve the energy efficiency of wireless sensors. 
  - **Delta encoding**: This is a lossless compression algorithm that encodes the difference between successive values, rather than the values themselves. It can reduce the redundancy in data with small variations. It is used in incremental backups, network protocols, and video coding.