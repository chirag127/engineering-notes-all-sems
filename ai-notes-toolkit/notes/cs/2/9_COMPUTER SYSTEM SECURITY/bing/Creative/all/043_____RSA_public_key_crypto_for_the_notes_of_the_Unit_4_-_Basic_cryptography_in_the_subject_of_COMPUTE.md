# RSA public key crypto

- RSA is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977.
- In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private). An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers are kept secret.
- RSA involves a public key and a private key. The public key can be known by everyone and is used for encrypting messages. The intention is that messages encrypted with the public key can only be decrypted in a reasonable amount of time by using the private key.
- The security of RSA relies on the computational difficulty of factoring large numbers. As of 2020, the largest public key for which the corresponding private key has been factored is 829 bits long.
- The basic steps of RSA are as follows:
  - Key generation:
    - Choose two distinct large prime numbers p and q.
    - Compute n = pq. n is the modulus for the public key and the private keys.
    - Compute φ(n) = (p − 1)(q − 1), where φ is Euler's totient function.
    - Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1; i.e., e and φ(n) are coprime. e is the public key exponent.
    - Compute d, the modular multiplicative inverse of e (mod φ(n)); i.e., solve for d the equation d⋅e ≡ 1 (mod φ(n)). d is the private key exponent.
    - The public key is (n, e) and the private key is (n, d). The values of p, q, and φ(n) must be kept secret.
  - Encryption:
    - To encrypt a message m, the sender computes c = m^e (mod n), where c is the ciphertext.
    - The sender transmits c to the receiver.
  - Decryption:
    - To decrypt a ciphertext c, the receiver computes m = c^d (mod n), where m is the plaintext.
    - The receiver recovers the original message m.