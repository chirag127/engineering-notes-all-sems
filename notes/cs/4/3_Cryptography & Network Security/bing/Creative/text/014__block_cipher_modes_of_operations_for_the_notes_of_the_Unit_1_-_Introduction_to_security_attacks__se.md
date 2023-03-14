### Block Cipher Modes of Operation

A block cipher is an encryption algorithm that takes a fixed size of input say b bits and produces a ciphertext of b bits again. If the input is larger than b bits it can be divided further. For different applications and uses, there are several modes of operations for a block cipher.  

Some of the common block cipher modes of operation are:

- **Electronic Code Book (ECB)**: This is the simplest mode of operation, where each block of input plaintext is encrypted independently with the same key and output is in form of blocks of encrypted ciphertext.  

  - Advantages: Parallel encryption of blocks of bits is possible, thus it is a faster way of encryption. Simple way of the block cipher. 
  - Disadvantages: Prone to cryptanalysis since there is a direct relationship between plaintext and ciphertext.  

- **Cipher Block Chaining (CBC)**: This is a more secure mode of operation, where the previous cipher block is given as input to the next encryption algorithm after XOR with the original plaintext block. This way, a cipher block is produced by encrypting an XOR output of the previous cipher block and present plaintext block.  

  - Advantages: CBC works well for input greater than b bits. CBC is a good authentication mechanism. Better resistive nature towards cryptanalysis than ECB. 
  - Disadvantages: Parallel encryption is not possible since every encryption requires a previous cipher.  

- **Cipher Feedback Mode (CFB)**: This is a mode of operation that can process data in blocks of any size. An initial vector IV is used for first encryption and output bits are divided as a set of s and b-s bits. The left-hand side s bits are selected along with plaintext bits to which an XOR operation is applied. The result is given as input to a shift register having b-s bits to lhs, s bits to rhs and the process continues.  

  - Advantages: Since, there is some data loss due to the use of shift register, thus it is difficult for applying cryptanalysis. 
  - Disadvantages: The drawbacks of CFB are the same as those of CBC mode. Both block losses and concurrent encryption of several blocks are not supported by the encryption. Decryption, however, is parallelizable and loss-tolerant. 

- **Output Feedback Mode (OFB)**: This is a mode of operation that follows nearly the same process as the Cipher Feedback mode except that it sends the encrypted output as feedback instead of the actual cipher which is XOR output.  

  - Advantages: OFB mode is similar to CFB mode, except that it is more resistant to transmission errors and can be used as a stream cipher. 
  - Disadvantages: OFB mode is vulnerable to plaintext attacks if the IV is reused. 

- **Counter Mode (CTR)**: This is a mode of operation that uses a counter, often constructed from a nonce and a block index, as the input and encrypts it with a block cipher. The result is XORed with the plaintext block to produce the ciphertext block. 

  - Advantages: CTR mode allows parallel encryption and decryption, and is resistant to transmission errors. It can also be used as a stream cipher. 
  - Disadvantages: CTR mode requires a unique counter for each block, otherwise it can be broken by a simple XOR operation. 

: Block cipher mode of operation - Wikipedia
: Block Cipher modes of Operation - GeeksforGeeks