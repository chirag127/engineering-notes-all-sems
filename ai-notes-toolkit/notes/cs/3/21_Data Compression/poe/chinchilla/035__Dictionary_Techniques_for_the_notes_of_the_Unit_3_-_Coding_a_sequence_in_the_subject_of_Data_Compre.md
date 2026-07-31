### Dictionary Techniques for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

In data compression, dictionary techniques are used to reduce the size of the data by encoding repeated patterns. Here are some important dictionary techniques that you need to know in order to understand data compression:

1. **Static Dictionary Technique:** 
   - This technique is based on a fixed set of patterns that are known in advance.
   - The encoder and decoder both have access to the same dictionary.
   - This technique is useful for compressing data that have a predictable structure, such as HTML pages or XML documents.

2. **Dynamic Dictionary Technique:**
   - This technique is based on building the dictionary on-the-fly as the data is being compressed.
   - The encoder and decoder both have access to the same dictionary, which is updated as new patterns are detected.
   - This technique is useful for compressing data that have a less predictable structure, such as natural language text.

3. **Adaptive Dictionary Technique:**
   - This technique is based on building the dictionary on-the-fly as the data is being compressed, but with the added feature of adaptability.
   - The encoder and decoder both have access to the same dictionary, which is updated as new patterns are detected and the frequency of patterns is tracked and updated.
   - This technique is useful for compressing data that have a highly variable structure, such as multimedia files.

4. **Lempel-Ziv-Welch (LZW) Compression Technique:**
   - This technique is based on building a dictionary of patterns that occur in the data.
   - The encoder and decoder both have access to the same dictionary, which is updated as new patterns are detected.
   - This technique is widely used in many compression algorithms, including GIF, TIFF, and PDF.

5. **Burrows-Wheeler Transform (BWT) Compression Technique:**
   - This technique is based on transforming the data into a form that is more easily compressed.
   - The encoder and decoder both have access to the same transformed data, which is then compressed using other techniques.
   - This technique is widely used in many compression algorithms, including bzip2 and the Unix compress command.

By understanding these dictionary techniques, you can better understand how data compression works and how to choose the best compression algorithm for your specific data.