### JPEG-LS

- JPEG-LS is a compression standard for continuous-tone images that supports both lossless and near-lossless modes  .
- JPEG-LS is based on the LOCO-I (LOw COmplexity LOssless COmpression for Images) algorithm developed at Hewlett-Packard Laboratories .
- JPEG-LS consists of two independent and distinct stages: modeling and encoding .
- Modeling stage predicts the value of each pixel based on its context (neighboring pixels) and computes the prediction error .
- Encoding stage compresses the prediction errors using a Golomb-Rice code, which is optimal for geometric distributions .
- JPEG-LS has a low complexity and high compression performance, especially for medical and scientific images .
- JPEG-LS is defined in two parts: ISO-14495-1/ITU-T.87 for the core technology and ISO-14495-2/ITU-T.870 for the extensions.
- JPEG-LS extensions include support for higher bit depths, progressive coding, region of interest coding, and arithmetic coding.

: https://en.wikipedia.org/wiki/Lossless_JPEG
: https://www.labs.hp.com/research/info_theory/loco/indexold.htm
: http://www.stat.columbia.edu/~jakulin/jpeg-ls/mirror.htm
: https://jpeg.org/jpegls/
: https://github.com/lnis-uofu/JPEG_LS