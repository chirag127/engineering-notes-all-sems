### Advanced Encryption Standard (AES) encryption and decryption

AES is a symmetric encryption algorithm that is widely used to secure data. It was developed by two Belgian cryptographers, Joan Daemen and Vincent Rijmen, and was adopted as a standard by the National Institute of Standards and Technology (NIST) in 2001.

#### How does AES work?

AES operates on 128-bit blocks of data and can use keys of 128, 192, or 256 bits. The encryption process involves several rounds of substitution, permutation, and mixing operations, which are designed to make it difficult for an attacker to recover the original data from the encrypted version.

The decryption process is essentially the reverse of the encryption process, but with the order of the operations reversed. To decrypt the data, the same key that was used to encrypt it must be used.

#### Advantages of AES

- AES is widely used and has been extensively analyzed, making it a trusted algorithm for securing data.
- It is computationally efficient and can be implemented in hardware or software.
- AES supports a range of key sizes, making it flexible for different use cases.
- It is resistant to various types of attacks, including brute force and differential cryptanalysis.

#### Disadvantages of AES

- The primary disadvantage of AES is that it is a symmetric encryption algorithm, which means that both the sender and receiver must have the same key. This can make key management challenging in some scenarios.

### Fermat’s and Euler’s theorem for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm

#### Fermat's theorem

Fermat's theorem states that if p is a prime number and a is an integer that is not divisible by p, then:

a^(p-1) ≡ 1 (mod p)

In other words, if we raise a to the power of p-1 and take the result modulo p, the result will be 1.

#### Euler's theorem

Euler's theorem is a generalization of Fermat's theorem that applies to any positive integer n and any integer a that is relatively prime to n. It states that:

a^φ(n) ≡ 1 (mod n)

where φ(n) is Euler's totient function, which gives the number of positive integers less than n that are relatively prime to n.

#### Applications of Fermat's and Euler's theorem

Fermat's and Euler's theorem are used in various cryptographic algorithms, including the RSA algorithm. They also have applications in number theory and other areas of mathematics.

### Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security

#### Principals of public key crypto systems

Public key cryptography is a type of cryptography that uses two keys, a public key and a private key. The public key is used to encrypt data, while the private key is used to decrypt it.

The main advantage of public key cryptography is that it allows secure communication between parties who have never met and do not share a secret key. This makes it well-suited for applications like secure email and online banking.

#### RSA algorithm

The RSA algorithm is a widely used public key cryptography algorithm that was invented by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977. It is named after their initials.

The RSA algorithm works by selecting two large prime numbers, p and q, and computing their product, n = p*q. A public key and a private key are then generated based on n and some other parameters. The public key consists of n and another number e, while the private key consists of n and another number d.

To encrypt a message using RSA, the sender first converts the message to a number and raises it to the power of e modulo n. The resulting number is the encrypted message. To decrypt the message, the receiver raises the encrypted message to the power of d modulo n.

#### Security of RSA

The security of RSA depends on the difficulty of factoring large numbers. If an attacker can factor n into its prime factors, then they can compute the private key and decrypt messages. However, factoring large numbers is believed to be a difficult problem, which makes RSA a secure algorithm for most practical purposes.