# Bi-level image compression-The JBIG standard

- Bi-level images are images that have only two possible pixel values, usually black and white.
- Bi-level image compression is the process of reducing the amount of data needed to represent a bi-level image, without losing any information or quality.
- The JBIG standard is an early lossless image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group, standardized as ISO/IEC 11544 and as ITU-T recommendation T.82 in March 1993.
- The JBIG standard is widely implemented in fax machines, and can also be used on other bi-level images.
- The JBIG standard offers between a 20% and 50% increase in compression efficiency over Fax Group 4 compression, and in some situations, it offers a 30-fold improvement.
- The JBIG standard uses a combination of arithmetic coding and adaptive template matching to achieve high compression ratios.
- The JBIG standard consists of three main components: the encoder, the decoder, and the arithmetic coder.
- The encoder divides the input image into stripes of 128 rows each, and processes each stripe independently.
- The encoder uses four modes to encode each stripe: typical prediction, generic region, symbol region, and refinement region.
- The typical prediction mode uses a fixed template to predict the value of each pixel based on its neighboring pixels, and encodes the prediction error using arithmetic coding.
- The generic region mode encodes a region of pixels that does not contain any symbols or halftones, using a variable template that adapts to the local image characteristics.
- The symbol region mode encodes a region of pixels that contains symbols or halftones, using a dictionary of symbols that is built dynamically during the encoding process.
- The refinement region mode encodes a region of pixels that is similar to a previously encoded region, using a refinement template that improves the quality of the reconstructed image.
- The decoder performs the inverse operations of the encoder, using the same arithmetic coder and the same modes to decode each stripe.
- The arithmetic coder is a binary adaptive arithmetic coder that assigns probabilities to each symbol based on the previous symbols and the context.
- The arithmetic coder uses a table of 4096 contexts, each of which has two probability estimates, one for the symbol 0 and one for the symbol 1.
- The arithmetic coder updates the probability estimates after each symbol is encoded or decoded, using a simple adaptation algorithm.
- The arithmetic coder also uses a bypass mode to encode or decode symbols with equal probabilities, without updating the probability estimates.