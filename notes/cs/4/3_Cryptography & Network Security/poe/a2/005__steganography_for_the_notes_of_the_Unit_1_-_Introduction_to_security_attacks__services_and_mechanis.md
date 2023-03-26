 Here are the notes on steganography for the given topic:

### Steganography
- Steganography is the art and science of hiding the existence of the communication. It hides the secret message into an ordinary message (called cover message or carrier) and transmits it. The intention is to conceal the very existence of the message and to make the medium carrying the secret message look innocent.
- The key requirements of a good steganographic system are:
- Imperceptibility: The embedded message should not be detectable by unauthorized persons.
- Security: The system should be robust against attempts to destroy the hidden information or extract the secret message from the steganographed data.
- Payload: The amount of secret information that can be embedded should be reasonably large.
- Some of the common steganography techniques are:
- Embedding data in images: Here the secret information is embedded into an image file format like BMP, GIF, PNG, etc. The color values of the pixels are altered slightly to embed data. The changes are perceptually indiscernible, but the secret data can be extracted with a key.
- Covering data with other data: The secret message can be first encrypted and then covered by an innocent looking cover message like a spam email, network traffic, etc. The ciphertext is padded and merged with the cover message. The receiver then extracts the secret message using the key and decrypts it.
- Use of Invisible ink: Though very old technique but still used. The secret ink is used to write the secret message and then it is made visible using some chemical. The visibility can be again hidden to make it secret.

Thus, steganography serves as a potential tool for secure communication along with cryptography. However, steganography can be misused for illegal activities like copyright infringement, pornography, etc. Proper laws and regulations are required to prevent such misuse.