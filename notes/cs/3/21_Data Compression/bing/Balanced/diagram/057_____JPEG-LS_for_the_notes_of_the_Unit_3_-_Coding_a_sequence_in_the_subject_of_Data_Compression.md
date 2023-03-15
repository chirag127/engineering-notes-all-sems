### JPEG-LS

- JPEG-LS is a compression standard for continuous-tone images that supports both lossless and near-lossless modes  .
- It is based on the LOCO-I (LOw COmplexity LOssless COmpression for Images) algorithm developed at Hewlett-Packard Laboratories .
- It consists of two independent and distinct stages: modeling and encoding  .
- The modeling stage predicts the value of each pixel based on its context (neighboring pixels) and computes the prediction error  .
- The encoding stage maps the prediction error to a symbol and encodes it using a Golomb-Rice code  .
- JPEG-LS has several advantages over other lossless compression methods, such as:
  - It is simple and efficient, requiring low computational complexity and memory  .
  - It adapts to local image characteristics, achieving high compression ratios for natural images  .
  - It supports progressive and interlaced coding, as well as region-of-interest coding.
  - It is robust to transmission errors and allows random access to the compressed data.
- JPEG-LS is defined in two parts: ISO/IEC 14495-1:1999 | ITU-T Rec. T.87 (1998), defining the core technology, and ISO/IEC 14495-2:2003 | ITU-T Rec. T.870 (03/2002), containing the extensions.