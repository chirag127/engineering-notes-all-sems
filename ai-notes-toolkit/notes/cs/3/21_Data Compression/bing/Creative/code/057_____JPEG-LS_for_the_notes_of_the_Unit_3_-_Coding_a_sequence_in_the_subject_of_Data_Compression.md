### JPEG-LS

- JPEG-LS is a compression standard for continuous-tone images that supports both lossless and near-lossless modes  .
- It is based on the LOCO-I (LOw COmplexity LOssless COmpression for Images) algorithm developed at Hewlett-Packard Laboratories .
- It consists of two independent and distinct stages: modeling and encoding  .
- The modeling stage predicts the value of each pixel based on its context (neighboring pixels) and computes the prediction error  .
- The encoding stage maps the prediction error to a symbol and encodes it using a Golomb-Rice code  .
- The standard defines four types of contexts: run, regular, edge, and corner  .
- The standard also defines two types of coding modes: near-lossless and lossless  .
- The near-lossless mode allows a small amount of error (specified by a parameter) in the reconstructed image, which can improve the compression ratio  .
- The lossless mode guarantees an exact reconstruction of the original image, which can preserve the image quality  .
- JPEG-LS is suitable for applications that require high fidelity, low complexity, and fast compression and decompression of continuous-tone images  .