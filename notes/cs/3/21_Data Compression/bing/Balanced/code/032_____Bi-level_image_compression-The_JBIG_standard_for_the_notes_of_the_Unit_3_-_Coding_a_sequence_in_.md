### Bi-level image compression-The JBIG standard

- Bi-level images are images that have only two possible pixel values, usually black and white.
- Bi-level image compression is the process of reducing the amount of data needed to represent a bi-level image.
- The JBIG standard (also known as JBIG1) is an early lossless image compression standard from the Joint Bi-level Image Experts Group, standardized as ISO/IEC 11544 and as ITU-T recommendation T.82 in March 1993.
- The JBIG standard is widely implemented in fax machines, as it offers better compression efficiency than Fax Group 4 compression, which is based on run-length encoding.
- The JBIG standard uses a technique called arithmetic coding, which assigns variable-length codes to symbols based on their probabilities of occurrence.
- The JBIG standard also uses a technique called adaptive template matching, which adapts the coding context to the local image features, such as edges, corners, and textures.
- The JBIG standard can compress bi-level images of any size and resolution, and can handle multiple images in a single file.
- The JBIG standard has some limitations, such as:
  - It cannot compress color or grayscale images, only bi-level images.
  - It cannot exploit the redundancy between similar images, such as pages of a document.
  - It cannot perform lossy compression, which may be desirable for some applications.

### Bi-level image compression-The JBIG2 standard

- The JBIG2 standard (also known as JBIG2) is a newer image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group, standardized as ISO/IEC 14492 and as ITU-T recommendation T.88 in 2000.
- The JBIG2 standard is suitable for both lossless and lossy compression, and can achieve much higher compression ratios than the JBIG standard, especially for text and halftone images .
- The JBIG2 standard uses a technique called model-based coding, which segments the image into regions of different types, such as text, halftone, and generic, and encodes them separately using different models.
- The JBIG2 standard also uses a technique called symbol dictionary coding, which identifies and stores the recurring symbols (such as characters or patterns) in the image, and encodes them using a shared dictionary.
- The JBIG2 standard can compress bi-level images of any size and resolution, and can handle multiple images in a single file.
- The JBIG2 standard can also exploit the redundancy between similar images, such as pages of a document, by using a technique called refinement coding, which encodes the differences between a reference image and a target image.
- The JBIG2 standard has some advantages, such as:
  - It can compress color or grayscale images, by converting them to bi-level images using a technique called halftoning.
  - It can perform lossy compression, by discarding some details or noise in the image, which may improve the visual quality or the compression ratio.
  - It can achieve very high compression ratios, up to 30 times better than the JBIG standard, for some types of images.