### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group  .
- Bi-level images are images that have only two colors, usually black and white, such as scanned documents, faxes, or text.
- JBIG2 is suitable for both lossless and lossy compression  .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 can achieve higher compression ratios than existing standards, such as MH&MR (ITU-T T.4), MMR (ITU-T T.6), and JBIG1 (T.82| ISO/IEC 11544), by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- Pattern matching and substitution techniques involve segmenting an image into overlapping and/or non-overlapping regions of text, halftone and generic content, and then compressing each region with a different method.
- Text regions are compressed by identifying and encoding recurring symbols, such as characters or words, and then using a dictionary to store and reference them.
- Halftone regions are compressed by detecting and removing the halftone screen, and then encoding the remaining gray-level image with a suitable method.
- Generic regions are compressed by applying a context-based arithmetic coding scheme, similar to JBIG1, but with improved contexts and adaptive templates.
- JBIG2 can also support progressive decoding, which means that a low-resolution or low-quality version of the image can be displayed before the full image is available.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.