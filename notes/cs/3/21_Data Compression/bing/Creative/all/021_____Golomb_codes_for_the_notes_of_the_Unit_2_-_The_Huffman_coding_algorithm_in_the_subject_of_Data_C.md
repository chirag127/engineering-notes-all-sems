Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on Golomb codes for the Unit 2 - The Huffman coding algorithm in the subject of Data Compression.

# Golomb codes

- Golomb codes are a type of prefix codes that are optimal for a geometric distribution of the source symbols.
- Golomb codes are parametric, meaning that they depend on a positive integer parameter m that determines the code length and distribution.
- Golomb codes can be used to compress data that has a Zipf-like distribution, such as natural language text, images, audio, or video.
- Golomb codes have two parts: a unary quotient and a binary remainder.
- The unary quotient is a sequence of q zeros followed by a one, where q is the integer part of n/m, and n is the source symbol to be encoded.
- The binary remainder is the binary representation of r, where r is the remainder of n/m, and has a variable length depending on m.
- The length of the binary remainder is either ⌊log₂m⌋ or ⌈log₂m⌉ bits, depending on whether m is a power of 2 or not.
- If m is a power of 2, then the binary remainder has a fixed length of log₂m bits, and the Golomb code is equivalent to a truncated binary code.
- If m is not a power of 2, then the binary remainder has a variable length, and the Golomb code can be further optimized by using a Rice code, which splits the possible values of r into two subsets of equal size.
- The Rice code assigns ⌊log₂m⌋ bits to the first subset and ⌈log₂m⌉ bits to the second subset, and uses an extra bit to indicate which subset r belongs to.
- The Rice code reduces the expected code length by 1/2 bit per symbol, compared to the Golomb code.
- The optimal value of m for a given source distribution can be calculated by minimizing the expected code length, or by using a heuristic such as m = ⌈-1/log₂(1-p)⌉, where p is the probability of the most frequent symbol.