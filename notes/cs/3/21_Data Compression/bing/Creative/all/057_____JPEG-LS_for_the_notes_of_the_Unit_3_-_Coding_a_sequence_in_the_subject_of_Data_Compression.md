# JPEG-LS

- JPEG-LS is a compression standard for continuous-tone images that supports both lossless and near-lossless modes  .
- JPEG-LS is based on the LOCO-I (LOw COmplexity LOssless COmpression for Images) algorithm developed at Hewlett-Packard Laboratories .
- JPEG-LS consists of two independent and distinct stages: modeling and encoding .
- In the modeling stage, JPEG-LS predicts the value of each pixel based on its neighboring pixels and computes the prediction error .
- In the encoding stage, JPEG-LS encodes the prediction error using a context-based adaptive Golomb-Rice code .
- JPEG-LS achieves high compression performance by exploiting the local correlation and smoothness of natural images .
- JPEG-LS has low complexity and memory requirements, making it suitable for embedded and real-time applications .
- JPEG-LS is defined in two parts: ISO/IEC 14495-1:1999 | ITU-T Rec. T.87 (1998), which specifies the core technology, and ISO/IEC 14495-2:2003 | ITU-T Rec. T.870 (03/2002), which contains the extensions.
- JPEG-LS extensions include support for progressive coding, hierarchical coding, region of interest coding, and arithmetic coding.
- JPEG-LS is compatible with the JPEG File Interchange Format (JFIF) and the JPEG 2000 File Format (JP2) for storing and exchanging compressed images.