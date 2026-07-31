Hello, I am Sydney, your AI assistant. I can help you with your study material on cryptography and network security. Here is some content on steganography for the notes of the Unit 1.

# Steganography

- Steganography is the art and science of hiding information in plain sight, such that only the intended recipient can detect it.
- Steganography can be used to conceal the existence of a secret message, or to enhance the security of an encrypted message by adding another layer of obfuscation.
- Steganography can be applied to various types of media, such as text, images, audio, video, or network protocols.
- Steganography techniques can be classified into two categories: **spatial domain** and **frequency domain**.
  - Spatial domain techniques modify the least significant bits (LSB) of the pixels or bits of the cover media, such as changing the color or brightness of an image, or inserting hidden characters in a text.
  - Frequency domain techniques transform the cover media into a different representation, such as discrete cosine transform (DCT) or discrete wavelet transform (DWT), and embed the secret message in the coefficients of the transformed domain, such as the high-frequency or low-frequency components of an image or audio.
- Steganography can be combined with cryptography to achieve **steganalysis-resistant** steganography, where the secret message is first encrypted and then hidden in the cover media, making it harder for an attacker to detect or recover the hidden information.
- Steganography can also be combined with **error correction codes** (ECC) to achieve **robust** steganography, where the secret message can be recovered even if the cover media is distorted or corrupted by noise, compression, or manipulation.
- Steganography can be evaluated by several criteria, such as **capacity**, **imperceptibility**, **security**, and **robustness**.
  - Capacity is the amount of information that can be hidden in the cover media without affecting its quality or size.
  - Imperceptibility is the degree to which the cover media is indistinguishable from the original media after hiding the secret message.
  - Security is the resistance to steganalysis, or the difficulty of detecting the presence or extracting the content of the hidden message by an unauthorized party.
  - Robustness is the ability to recover the hidden message after the cover media undergoes some transformations, such as noise, compression, or manipulation.