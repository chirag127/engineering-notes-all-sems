 Here are the notes in markdown format without emojis or external links and in a formal tone:

### JBIG2 for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. JBIG2 is an image compression standard for bi-level images developed by the Joint Bi-level Image Experts Group committee.
2. It is suitable for compressing scanned documents, particularly those containing text or line art.
3. JBIG2 encodes regions of identical pixels through pattern matching and substitution. It can match patterns even if they are shifted or rotated versions of each other.
4. The algorithm segments the image into regions and encodes each region using a selected pattern from a dictionary. The encoder searches for the best match for a region's pixels in the dictionary. If no good enough match is found, a new pattern is added to the dictionary to represent the region.
5. The JBIG2 standard supports lossless and lossy compression. The lossy mode enables higher compression ratios at the cost of some loss of quality. The amount of loss can be controlled by adjusting parameters.
6. JBIG2 is more efficient than older algorithms like Modified Huffman coding and Cross block pattern coding as it utilizes similarities across wider areas, not just individual lines. It gives much higher compression ratios for bi-level images containing text and line art.

The above notes cover the key points about JBIG2 image compression standard and its working in a formal tone with points and without emojis or external links as requested. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.