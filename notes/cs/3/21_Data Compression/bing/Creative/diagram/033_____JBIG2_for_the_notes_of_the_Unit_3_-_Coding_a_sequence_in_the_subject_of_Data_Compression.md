### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group   .
- Bi-level images are images that have only two possible values for each pixel, such as black and white.
- JBIG2 is suitable for both lossless and lossy compression  .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 typically generates files 3–5 times smaller than Fax Group 4 and 2–4 times smaller than JBIG, the previous standards for bi-level image compression.
- JBIG2 can also achieve much higher compression ratios than the previous standards with almost no visible degradation of quality by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- JBIG2 works by segmenting an image into overlapping and/or non-overlapping regions of text, halftone and generic content, and applying compression techniques that are specially optimized for each type of content.
- Text regions are further divided into symbols, which are matched with a symbol dictionary. The dictionary can be either predefined or dynamically generated from the image. The symbols are then encoded by referring to their dictionary index or by using arithmetic coding.
- Halftone regions are compressed by detecting the halftone pattern and encoding it as a single bitmap, along with the parameters of the grid. The bitmap is then compressed using arithmetic coding.
- Generic regions are compressed using a modified version of the JBIG algorithm, which is based on arithmetic coding and adaptive template switching.
- JBIG2 also supports progressive decoding, refinement coding, and arithmetic coding with adaptive probability estimation.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.