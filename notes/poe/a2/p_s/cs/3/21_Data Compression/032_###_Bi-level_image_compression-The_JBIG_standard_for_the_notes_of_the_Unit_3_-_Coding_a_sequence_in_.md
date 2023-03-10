 Here is the content in markdown format for the given topic:

### Bi-level image compression-The JBIG standard

- JBIG is a lossless bi-level image compression standard. It is suitable for compressing scanned documents like text documents, engineering drawings, etc.
- JBIG stands for Joint Bi-level Image Experts Group. It was developed by ISO/ITU in the early 1990s.
- JBIG uses an arithmetic coding technique which can achieve better compression than other bi-level compression techniques like MMR, MR, MH, etc.
- The key stages in JBIG compression are:

1. Prediction - Neighboring pixels are used to predict the next pixel value. The difference between the actual and predicted value is encoded. This reduces the entropy and increases compression.
2. Pattern matching - The incoming pixel stream is matched with a set of template patterns. The template index is encoded instead of the raw pixel values. This further reduces entropy.
3. Arithmetic coding - The remaining data is arithmetically encoded to achieve lossless compression.

- Advantages:
 - Lossless compression. No information is lost.
 - High compression ratio for bi-level images.
 - Fast decompression.
- Applications:
 - Fax machines.
 - Scanned document storage and transmission.

[Include relevant diagrams, examples, codes, tables, etc here if any.]

- The content here summarizes the key points about bi-level JBIG image compression standard which can be helpful to learn and read from for exams. Please let me know if you would like me to elaborate on any of the points or add more details to the content.