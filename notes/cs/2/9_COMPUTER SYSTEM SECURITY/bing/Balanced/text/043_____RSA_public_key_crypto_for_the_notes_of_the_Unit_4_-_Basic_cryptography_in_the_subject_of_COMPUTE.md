### RSA public key crypto

RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977.

In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private). An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers are kept secret.

RSA involves a public key and a private key. The public key can be known by everyone and is used for encrypting messages. The intention is that messages encrypted with the public key can only be decrypted in a reasonable amount of time by using the private key.

The main steps of RSA algorithm are:

- Key generation: The RSA user chooses two large prime numbers p and q, and computes their product n = pq, which is called the modulus. The user also chooses a small number e, which is the public exponent, and is coprime to (p-1)(q-1). The user then computes d, which is the private exponent, such that ed ≡ 1 (mod (p-1)(q-1)). The public key is (n, e) and the private key is (n, d).
- Encryption: The sender of the message m computes the ciphertext c as c = m^e (mod n) and sends it to the receiver.
- Decryption: The receiver of the ciphertext c computes the plaintext m as m = c^d (mod n) using the private key.

The security of RSA relies on the difficulty of factoring large numbers. If an attacker can factor n into p and q, then they can compute d and decrypt the ciphertext. However, no efficient algorithm for factoring large numbers is known, and the problem is believed to be hard .

Here is an example of RSA encryption and decryption:

- Key generation: Suppose p = 53 and q = 59 are the prime numbers. Then n = pq = 3127 and (p-1)(q-1) = 3016. Suppose e = 3 is the public exponent. Then d = 2011 is the private exponent, since ed ≡ 1 (mod (p-1)(q-1)). The public key is (3127, 3) and the private key is (3127, 2011).
- Encryption: Suppose the message m = 89. Then the ciphertext c is c = m^e (mod n) = 89^3 (mod 3127) = 1394.
- Decryption: Suppose the ciphertext c = 1394. Then the plaintext m is m = c^d (mod n) = 1394^2011 (mod 3127) = 89.