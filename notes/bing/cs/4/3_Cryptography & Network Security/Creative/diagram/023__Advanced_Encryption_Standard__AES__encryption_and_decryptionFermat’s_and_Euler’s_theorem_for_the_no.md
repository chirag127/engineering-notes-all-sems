The following diagram illustrates the basic architecture of AES encryption and decryption using ASCII characters:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Plaintext     |     |  Ciphertext    |     |  Plaintext     |
|                |     |                |     |                |
+-------+--------+     +--------+-------+     +--------+-------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
+-------v--------+     +--------v-------+     +--------v-------+
|                |     |                |     |                |
|  Key Expansion |     |  Key Expansion |     |  Key Expansion |
|                |     |                |     |                |
+-------+--------+     +--------+-------+     +--------+-------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
+-------v--------+     +--------v-------+     +--------v-------+
|                |     |                |     |                |
|  Encryption    |     |  Decryption    |     |  Encryption    |
|                |     |                |     |                |
+-------+--------+     +--------+-------+     +--------+-------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
+-------v--------+     +--------v-------+     +--------v-------+
|                |     |                |     |                |
|  Ciphertext    |     |  Plaintext     |     |  Ciphertext    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The AES algorithm is a symmetric block cipher that can encrypt and decrypt information using the same key. The key is expanded into an array of key schedule words using a key expansion algorithm. The encryption and decryption processes consist of several rounds of substitution, transposition, and mixing operations on the input data, which is divided into blocks of 128 bits. The number of rounds depends on the key size: 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys. Each round uses a different subset of the key schedule words. The encryption and decryption algorithms are inverse of each other, meaning that the order of the operations is reversed and the inverse functions are used. The AES algorithm is designed to be secure, efficient, and easy to implement in hardware and software.     

Fermat's and Euler's theorems are mathematical results that relate the modular arithmetic of prime and relative prime numbers to the group and field structures of finite fields. A group is a set of elements with a binary operation that satisfies certain properties, such as closure, associativity, identity, and inverse. A field is a group that also has a second binary operation that satisfies additional properties, such as commutativity, distributivity, and nonzero inverse. A finite field is a field that has a finite number of elements. A finite field of the form GF(p) is a field with p elements, where p is a prime number. The elements of GF(p) are the integers from 0 to p-1, and the operations are addition and multiplication modulo p.  

Fermat's theorem states that if p is a prime number and a is any integer that is not divisible by p, then a^(p-1) is congruent to 1 modulo p. That is, a^(p-1) mod p = 1. This theorem can be used to test whether a number is prime or not, by checking if the equation holds for