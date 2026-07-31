### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group  .
- Bi-level images are images that have only two possible values for each pixel, such as black and white.
- JBIG2 is suitable for both lossless and lossy compression  .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 typically generates files 3–5 times smaller than Fax Group 4 and 2–4 times smaller than JBIG, the previous standards for bi-level image compression, in its lossless mode.
- JBIG2 can also achieve much higher compression ratios than the previous standards in its lossy mode, with almost no visible degradation of quality, by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- JBIG2 works by segmenting an image into overlapping and/or non-overlapping regions of text, halftone and generic content, and applying compression techniques that are specially optimized for each type of content.
- Text regions are compressed by identifying and encoding recurring symbols, such as characters or words, and using a dictionary to store them.
- Halftone regions are compressed by identifying and encoding the shape and position of the halftone dots, which are used to create shades of gray or color in printing.
- Generic regions are compressed by using arithmetic coding or MMR (Modified Modified READ), which are entropy coding methods that exploit the statistical properties of the data.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.
- JBIG2 is widely used in document imaging, such as scanning, faxing, and PDF files.