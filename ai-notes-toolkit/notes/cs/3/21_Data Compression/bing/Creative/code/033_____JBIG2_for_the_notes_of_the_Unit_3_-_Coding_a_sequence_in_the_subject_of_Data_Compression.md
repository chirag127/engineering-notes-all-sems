### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group .
- Bi-level images are images that have only two possible values for each pixel, such as black and white.
- JBIG2 is suitable for both lossless and lossy compression .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 typically generates files 3–5 times smaller than Fax Group 4 and 2–4 times smaller than JBIG, the previous standards for bi-level image compression .
- JBIG2 can achieve much higher compression ratios than the previous standards by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- Pattern matching and substitution means that JBIG2 can identify and group similar regions of an image, such as characters or symbols, and assign them a unique code. Then, instead of storing the pixel values of each region, JBIG2 can store only the code and the location of each region.
- JBIG2 can segment an image into overlapping and/or non-overlapping regions of text, halftone and generic content, and apply compression techniques that are specially optimized for each type of content .
- Text regions are compressed by using a dictionary of symbols and a refinement coding method that encodes the differences between similar symbols.
- Halftone regions are compressed by using a template matching method that encodes the periodicity and the phase of the halftone pattern.
- Generic regions are compressed by using a context-based arithmetic coding method that encodes the pixel values based on the surrounding pixels.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.
- JBIG2 is widely used for compressing scanned documents, such as PDF files, and is supported by many software applications and hardware devices .