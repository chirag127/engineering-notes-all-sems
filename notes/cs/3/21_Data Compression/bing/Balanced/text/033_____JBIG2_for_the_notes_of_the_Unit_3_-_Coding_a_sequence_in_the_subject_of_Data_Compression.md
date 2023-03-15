### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group  .
- Bi-level images are images that have only two colors, usually black and white, such as scanned documents, faxes, or text.
- JBIG2 is suitable for both lossless and lossy compression  .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 can achieve higher compression ratios than the existing standards, such as MH&MR (ITU-T T.4), MMR (ITU-T T.6), and JBIG1 (T.82| ISO/IEC 11544), by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- Pattern matching and substitution techniques involve segmenting an image into overlapping and/or non-overlapping regions of text, halftone, and generic content, and then compressing each region using different methods.
- Text regions are compressed by identifying and encoding recurring symbols, such as characters or words, and then replacing them with references to a symbol dictionary.
- Halftone regions are compressed by identifying and encoding the shape and position of the halftone dots, and then replacing them with references to a halftone dictionary.
- Generic regions are compressed by using arithmetic coding or MMR, depending on the image quality and compression ratio desired.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.