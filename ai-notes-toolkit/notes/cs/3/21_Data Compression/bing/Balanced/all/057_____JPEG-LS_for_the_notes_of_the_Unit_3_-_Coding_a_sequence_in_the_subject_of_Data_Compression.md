# JPEG-LS

- JPEG-LS is a **lossless/near-lossless compression standard** for continuous-tone images .
- Its official designation is **ISO-14495-1/ITU-T.87**   .
- It is based on the **LOCO-I** algorithm (LOw COmplexity LOssless COmpression for Images) developed at **Hewlett-Packard Laboratories** .
- It consists of two independent and distinct stages called **modeling** and **encoding** .
- The modeling stage predicts the value of each pixel based on its **local context** (the neighboring pixels) and computes the **prediction error**  .
- The encoding stage maps the prediction error to a **symbol** and encodes it using a **context-based adaptive arithmetic coder**  .
- JPEG-LS can achieve **high compression ratios** and **low complexity** compared to other lossless compression methods   .
- JPEG-LS also supports **near-lossless compression**, which allows a small amount of distortion (controlled by a parameter) in exchange for higher compression ratios .
- JPEG-LS has two parts: the **core** and the **extensions**.
- The core defines the basic algorithm and the syntax for the compressed data stream.
- The extensions define additional features such as **progressive coding**, **hierarchical coding**, **region of interest coding**, and **multi-component coding**.