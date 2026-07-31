### JPEG-LS

- JPEG-LS is a compression standard for continuous-tone images that supports both lossless and near-lossless modes .
- JPEG-LS is based on the LOCO-I algorithm (LOw COmplexity LOssless COmpression for Images) developed at Hewlett-Packard Laboratories.
- JPEG-LS consists of two independent and distinct stages: modeling and encoding .
- Modeling stage: predicts the value of each pixel based on its context (neighboring pixels) and computes the prediction error .
- Encoding stage: encodes the prediction error using a Golomb-Rice code, which adapts to the local statistics of the error distribution .
- JPEG-LS has low complexity, high compression performance, and fast encoding and decoding .
- JPEG-LS is defined in two parts: ISO/IEC 14495-1:1999 | ITU-T Rec. T.87 (1998), which defines the core technology, and ISO/IEC 14495-2:2003 | ITU-T Rec. T.870 (03/2002), which contains the extensions.
- JPEG-LS extensions include: region of interest coding, hierarchical coding, progressive coding, and arithmetic coding.
- JPEG-LS is suitable for applications that require high-quality images, such as medical imaging, remote sensing, and archival.