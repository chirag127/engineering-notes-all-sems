### RSA public key crypto

RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977.

In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private). An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers are kept secret.

RSA involves a public key and a private key. The public key can be known by everyone and is used for encrypting messages. The intention is that messages encrypted with the public key can only be decrypted in a reasonable amount of time by using the private key.

The main steps of the RSA algorithm are as follows:

- Key generation
  - Choose two distinct large prime numbers p and q.
  - Compute n = pq. n is the modulus for the public key and the private keys.
  - Compute φ(n) = (p − 1)(q − 1), where φ is Euler's totient function.
  - Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1; i.e., e and φ(n) are coprime. e is the public key exponent.
  - Determine d as d ≡ e−1 (mod φ(n)); i.e., d is the multiplicative inverse of e (modulo φ(n)). d is the private key exponent.
  - The public key consists of the modulus n and the public (or encryption) exponent e. The private key consists of the modulus n and the private (or decryption) exponent d, which must be kept secret.
- Encryption
  - To encrypt a message m, the sender computes the ciphertext c as c = m^e mod n, where m is the message represented as an integer in the range [0, n − 1].
  - The sender then transmits c to the receiver.
- Decryption
  - To decrypt the ciphertext c, the receiver computes the plaintext m as m = c^d mod n, where d is the private key exponent.
  - The receiver can recover the original message m from the ciphertext c using the private key.

The security of RSA relies on the difficulty of factoring large numbers. If an attacker can factor n into p and q, then they can compute φ(n) and d, and thus break the encryption. However, no efficient algorithm for factoring large numbers is known, and the best known methods take exponential time in the size of n.

RSA encryption is widely used for data encryption of e-mail and other digital transactions over the Internet. It is also used for digital signatures, which can verify the authenticity and integrity of a message.