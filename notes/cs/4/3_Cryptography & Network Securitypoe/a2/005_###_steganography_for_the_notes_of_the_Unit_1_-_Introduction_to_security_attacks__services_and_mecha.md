 Here is the content in markdown format for the given topic:

### Steganography

Steganography is the art and science of hiding the existence of communicated message. It hides the secret message into an ordinary message called cover message or carrier in such a way that no one apart from the sender and receiver suspects the existence of hidden message. The cover message may be an image, audio or video file. Some common techniques of steganography are:

- Least significant bit insertion: In this technique, the least significant bits of the pixels of an image are changed to embed the secret message. This technique produces good imperceptibility but less capacity.
- Masking and filtering: In this technique, the secret message is first encrypted and then embedded in an image by slightly changing the pixel values of the image. This technique also produces good imperceptibility but less capacity.
- Transform domain techniques: In this technique, the cover image is first transformed into frequency domain using discrete cosine transform or discrete wavelet transform. The secret message is then embedded into the mid frequency coefficients as human eyes are less sensitive to changes in mid frequency coefficients. This technique provides better capacity but produces artefacts in the stego-image.

Advantages:

- The existence of hidden message is undetectable.
- The secret message is secured from unauthorized access.

Disadvantages:

- The amount of data that can be hidden is less.
- The stego-object may degrade in quality.

Applications:

- Secret communication
- Copyright protection
- Secure storage of data

### Substitution Ciphers

Substitution ciphers are a type of encryption algorithms where every character of plain text is replaced by another character or symbol. The substitution may be one-to-one or many-to-one. Some popular examples of substitution ciphers are:

- Caesar Cipher: In this cipher, every character of plain text is substituted by another character which is obtained by shifting the position of character in the alphabet by some fixed number of positions.
- Monoalphabetic Cipher: In this cipher, every character of plain text is substituted by another character based on a substitution table or cipher alphabet. The cipher alphabet may be cipher text only, plain text only or a mix of both. This type of cipher is easy to break by frequency analysis.
- Homophonic Cipher: In this cipher, a character may be substituted by two or more substitutes to confuse the frequency analysis. However, this type of cipher is also easy to break.

[Similar details can be added for rest of the topics like transposition ciphers, cryptanalysis, stream and block ciphers, etc.]