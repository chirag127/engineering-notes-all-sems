### Modular arithmetic

Modular arithmetic is a system of arithmetic for integers, where values reset to zero and begin to increase again, after reaching a certain predefined value, called the modulus (modulo). Modular arithmetic is widely used in computer science and cryptography.

- Definition: Let ZN be a set of all non-negative integers that are smaller than N:

ZN = {0, 1, 2, ..., N-1}

Modular arithmetic is the arithmetic of the elements of ZN. The modulus N is fixed and we write:

a mod N

to denote the remainder of the division of a by N. For example, if N = 5, then:

7 mod 5 = 2

because 7 = 5 * 1 + 2, and 2 is the remainder.

- Properties: Modular arithmetic has some basic properties that are similar to the usual arithmetic, such as:

(a + b) mod N = (a mod N + b mod N) mod N

(a - b) mod N = (a mod N - b mod N) mod N

(a * b) mod N = (a mod N * b mod N) mod N

However, modular arithmetic does not have the property of division, because not every element in ZN has a multiplicative inverse. For example, if N = 6, then:

2 * 3 mod 6 = 0

but there is no x such that:

0 * x mod 6 = 1

- Applications: Modular arithmetic is essential for many cryptographic algorithms, such as:

  - RSA: RSA is a public key cryptosystem that relies on the difficulty of factoring large numbers. RSA uses modular arithmetic to generate public and private keys, encrypt and decrypt messages, and sign and verify signatures. For example, to encrypt a message m using a public key (e, n), where n is the product of two large primes p and q, we compute:

    c = m^e mod n

    where c is the ciphertext.

  - Diffie-Hellman: Diffie-Hellman is a key exchange protocol that allows two parties to establish a shared secret key over an insecure channel. Diffie-Hellman uses modular arithmetic to compute the secret key using a public base g, a public modulus p, and private exponents a and b. For example, Alice and Bob agree on g and p, and choose a and b randomly. Then they exchange:

    A = g^a mod p

    B = g^b mod p

    where A and B are public values. Then they can compute the secret key as:

    K = A^b mod p = B^a mod p = g^ab mod p

  - AES: AES is a symmetric key cipher that operates on blocks of 128 bits. AES uses modular arithmetic to perform various operations on the blocks, such as:

    - SubBytes: This operation substitutes each byte of the block with another byte, using a lookup table called the S-box. The S-box is constructed using modular arithmetic, by finding the multiplicative inverse of each byte in GF(2^8), and then applying an affine transformation. For example, to find the S-box value for the byte 0x53, we first compute its inverse in GF(2^8):

      0x53^-1 mod (x^8 + x^4 + x^3 + x + 1) = 0xCA

      where (x^8 + x^4 + x^3 + x + 1) is the irreducible polynomial used to define GF(2^8). Then we apply the affine transformation:

      S-box(0x53) = (0xCA * 0x1F) mod (x^8 + x^4 + x^3 + x + 1) + 0x63 = 0x8A

    - MixColumns: This operation mixes the columns of the block, by multiplying each column by a fixed matrix in GF(2^8). For example, to mix the first column of the block, we multiply it by the matrix:

      | 0x02 0x03 0x01 0x01 |

      | 0x01 0x02 0x03 0x01 |

      | 0x01 0x01 0x02 0x03 |

      | 0x03 0x01 0x01 0x02 |

      using modular arithmetic in GF(2^8). For example, to compute the first