# Classical encryption techniques

## Substitution ciphers and transposition ciphers

- Substitution ciphers are a type of encryption technique that replace each plaintext symbol with a different ciphertext symbol, according to a fixed rule or key.
- Transposition ciphers are a type of encryption technique that rearrange the order of the plaintext symbols, according to a fixed rule or key.
- Examples of substitution ciphers are Caesar cipher, monoalphabetic cipher, polyalphabetic cipher, and one-time pad.
- Examples of transposition ciphers are rail fence cipher, columnar transposition cipher, and permutation cipher.
- Substitution ciphers and transposition ciphers are both symmetric-key encryption techniques, meaning that the same key is used for encryption and decryption.
- Substitution ciphers and transposition ciphers are both vulnerable to cryptanalysis, which is the process of breaking the encryption and recovering the plaintext.

## Cryptanalysis

- Cryptanalysis is the science and art of breaking encryption schemes and recovering the plaintext from the ciphertext.
- Cryptanalysis can be performed by various methods, such as brute-force attack, frequency analysis, known-plaintext attack, chosen-plaintext attack, chosen-ciphertext attack, and differential cryptanalysis.
- Brute-force attack is a method of cryptanalysis that tries all possible keys until the correct one is found.
- Frequency analysis is a method of cryptanalysis that exploits the statistical patterns of the plaintext symbols in the ciphertext, such as the relative frequencies of letters in a natural language.
- Known-plaintext attack is a method of cryptanalysis that uses some pairs of plaintext and ciphertext that are known to the attacker, and tries to find the key or the encryption algorithm.
- Chosen-plaintext attack is a method of cryptanalysis that allows the attacker to choose some plaintexts and obtain their corresponding ciphertexts, and tries to find the key or the encryption algorithm.
- Chosen-ciphertext attack is a method of cryptanalysis that allows the attacker to choose some ciphertexts and obtain their corresponding plaintexts, and tries to find the key or the encryption algorithm.
- Differential cryptanalysis is a method of cryptanalysis that analyzes the differences between pairs of plaintexts and ciphertexts, and tries to find the key or the encryption algorithm.

## Steganography

- Steganography is the technique of hiding a secret message within another message, such as an image, a video, or an audio file, in such a way that the presence of the secret message is not noticeable.
- Steganography is different from encryption, as encryption makes the message unreadable, but not undetectable, while steganography makes the message undetectable, but not unreadable.
- Steganography can be used to enhance the security of encryption, by hiding the ciphertext within another message, making it harder for an attacker to find and analyze the ciphertext.
- Steganography can also be used to bypass censorship or surveillance, by concealing the content or the sender of the message within another message, making it harder for an authority to block or trace the message.
- Steganography can be performed by various methods, such as least significant bit (LSB) insertion, masking and filtering, transform domain techniques, and spread spectrum techniques.
- LSB insertion is a method of steganography that modifies the least significant bits of the pixels or samples of the cover message, such as an image or an audio file, to embed the secret message.
- Masking and filtering is a method of steganography that adds the secret message as a watermark or a noise to the cover message, such as an image or a video file, making it more resistant to compression or manipulation.
- Transform domain techniques are methods of steganography that embed the secret message in the frequency domain of the cover message, such as the discrete cosine transform (DCT) or the discrete wavelet transform (DWT) of an image or an audio file, making it more robust to noise or distortion.
- Spread spectrum techniques are methods of steganography that spread the secret message over a wide frequency band of the cover message, such as an audio or a radio signal, making it more difficult to detect or remove.

## Stream and block ciphers

- Stream ciphers and block ciphers are two types of symmetric-key encryption techniques that operate on different units of plaintext and ciphertext.
- Stream ciphers are a type of encryption technique that encrypt each plaintext symbol, such as a bit or a byte, individually, using a keystream that is generated from a secret key and an initialization vector (IV).
- Block ciphers are a type of encryption technique that encrypt each plaintext block, such as 64 bits or 128 bits, as a whole, using a secret key and a series of transformations, such as substitution and permutation.
- Examples of stream ciphers are RC4, A5/