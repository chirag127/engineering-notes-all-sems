### JPEG-LS

- JPEG-LS is a **lossless/near-lossless compression standard** for continuous-tone images .
- It is based on the **LOCO-I algorithm** (LOw COmplexity LOssless COmpression for Images) developed at Hewlett-Packard Laboratories.
- It consists of two independent and distinct stages called **modeling and encoding**.
- Modeling stage predicts the value of each pixel based on its context (neighboring pixels) and computes the prediction error.
- Encoding stage compresses the prediction error using a **context-based adaptive arithmetic coder**.
- JPEG-LS supports **lossless, near-lossless and lossy modes** of compression .
- Lossless mode preserves the exact pixel values of the original image.
- Near-lossless mode allows a small amount of distortion (controlled by a parameter) to achieve higher compression ratios.
- Lossy mode uses a **quantization step** to reduce the number of prediction errors before encoding.
- JPEG-LS is a **low-complexity algorithm** that matches JPEG 2000 compression ratios .
- It is suitable for applications that require high-quality images with low processing power and memory requirements .