### RSA public key crypto

- RSA is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977.
- In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private). An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers are kept secret.
- RSA involves a public key and a private key. The public key can be known by everyone and is used for encrypting messages. The intention is that messages encrypted with the public key can only be decrypted in a reasonable amount of time by using the private key.
- The basic steps of RSA algorithm are as follows:
  - Generate two large random prime numbers, p and q, of similar bit-length.
  - Compute n = p*q, where n is the modulus of the public and private keys.
  - Compute φ(n) = (p-1)*(q-1), where φ is Euler's totient function.
  - Choose an integer e such that 1 < e < φ(n) and e is co-prime to φ(n), i.e., e and φ(n) share no common factors except 1. e is the public key exponent.
  - Compute d such that d*e ≡ 1 (mod φ(n)), i.e., d is the multiplicative inverse of e modulo φ(n). d is the private key exponent.
  - The public key is (n, e) and the private key is (n, d). Keep the private key secret and distribute the public key.
  - To encrypt a message m, compute c = m^e (mod n), where c is the ciphertext.
  - To decrypt a ciphertext c, compute m = c^d (mod n), where m is the plaintext.
- RSA encryption is based on the mathematical problem of factoring large numbers, which is assumed to be hard. The security of RSA depends on the choice of large prime numbers and the length of the key. The larger the key, the harder it is to break the encryption.