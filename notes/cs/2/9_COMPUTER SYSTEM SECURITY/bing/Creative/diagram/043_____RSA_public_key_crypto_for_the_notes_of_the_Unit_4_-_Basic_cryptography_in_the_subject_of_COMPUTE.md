### RSA public key crypto

- RSA is a public-key cryptosystem that is widely used for secure data transmission.
- It is one of the oldest public-key cryptosystems, invented by Ron Rivest, Adi Shamir and Leonard Adleman in 1977.
- In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private).
- An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers are kept secret.
- The public key can be used by anyone to encrypt messages, which can only be decrypted by the private key holder.
- RSA is based on the mathematical problem of factoring large numbers, which is believed to be hard to solve efficiently.
- The security of RSA depends on the size of the key and the choice of the prime numbers.
- The key generation, encryption and decryption algorithms of RSA are as follows:

#### Key generation
- Choose two distinct large prime numbers p and q.
- Compute n = pq, which is the modulus of the public and private keys.
- Compute φ(n) = (p-1)(q-1), which is the Euler's totient function of n.
- Choose an integer e such that 1 < e < φ(n) and e is coprime to φ(n), which is the public exponent of the public key.
- Compute d such that de ≡ 1 (mod φ(n)), which is the private exponent of the private key. This can be done using the extended Euclidean algorithm.
- The public key is (n, e) and the private key is (n, d).

#### Encryption
- To encrypt a message m, where 0 < m < n, compute c = m^e (mod n), which is the ciphertext.
- To decrypt a ciphertext c, compute m = c^d (mod n), which is the original message.

#### Example
- Suppose p = 61 and q = 53, then n = 3233 and φ(n) = 3120.
- Suppose e = 17, which is coprime to 3120, then d = 2753, which satisfies de ≡ 1 (mod 3120).
- The public key is (3233, 17) and the private key is (3233, 2753).
- To encrypt a message m = 65, compute c = 65^17 (mod 3233) = 2790, which is the ciphertext.
- To decrypt the ciphertext c = 2790, compute m = 2790^2753 (mod 3233) = 65, which is the original message.