### authentication functions for the notes of the Unit 3 - Message Authentication Codes in the subject of Cryptography & Network Security
Message Authentication Codes (MACs) are cryptographic functions used to authenticate messages. They provide data integrity and authenticity by ensuring that the message has not been altered during transmission and that it was sent by the expected sender.

MACs use a shared secret key between the sender and receiver to generate a fixed-length code (the MAC) that is appended to the message. The receiver can then use the same key to verify the MAC and ensure the authenticity of the message.

There are two main types of MAC functions:
1. Hash-based MACs (HMACs)
2. Block-cipher-based MACs (CBC-MACs)

HMACs use a hash function and a secret key to generate the MAC. The hash function is applied to the message and the key, and the resulting hash value is used as the MAC.

CBC-MACs use a block cipher and a secret key to generate the MAC. The message is divided into blocks and each block is encrypted using the block cipher and the secret key. The final block is used as the MAC.

Both HMACs and CBC-MACs provide data integrity and authenticity, but HMACs are generally considered to be more secure due to the use of a hash function.
