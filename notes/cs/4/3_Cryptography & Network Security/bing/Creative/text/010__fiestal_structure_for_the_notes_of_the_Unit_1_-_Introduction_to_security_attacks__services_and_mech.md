### Feistel structure

- A Feistel structure is a symmetric structure used in the construction of block ciphers, named after the German-born physicist and cryptographer Horst Feistel who did pioneering research while working for IBM .
- A Feistel structure consists of iteratively running a function called a round function a fixed number of times on the data to be encrypted or decrypted .
- The round function takes two inputs: a data block and a subkey, and returns one output of the same size as the data block.
- In each round, the round function is run on half of the data, and its output is XORed with the other half of the data. Then, the halves are swapped for the next round .
- The final output is the encrypted or decrypted data, depending on the order of the subkeys .
- An advantage of Feistel structures is that they are guaranteed to be invertible, even if the round function is not itself invertible.
- A disadvantage of Feistel structures is that they are slower than other cipher designs, such as substitution-permutation networks, because they operate on half of the data at a time.
- Many block ciphers use the Feistel structure, such as DES, GOST, Blowfish, and Twofish .