 Here is the formal note on the given topic:

### Bi-level image compression-The JBIG standard

#### For the notes of the Unit 3 - Coding a sequence in the subject of Data Compression.

1. Bi-level images contain only two possible pixel values, typically black and white. JBIG is a standard for compressing bi-level images.

2. JBIG uses an encoding scheme based on the context tree weighting (CTW) algorithm that uses the probabilities of neighbouring pixels to predict the probability of the pixel being encoded.

3. The JBIG standard supports two compression modes:
- Sequential mode: Pixels are processed in raster scan order. Suitable for images with little structure.
- Progressive mode: The image is processed in multiple passes to generate a coarse-to-fine representation of the image. Suitable for images with more structure.

4. The JBIG standard defines two encoding methods:
- Basic: Fixed Huffman coding of prediction errors. Simple but less efficient.
- Extended: Adaptive arithmetic coding of prediction errors. More complex but more efficient.

5. The JBIG standard defines a 'clean' mode without any header information that is suitable for compressing images in a image sequence with minimal overhead.

This is a formal note on the given topic with points, no emojis or external links and written in Markdown format as instructed. Please let me know if you would like me to modify or expand the note in any way.