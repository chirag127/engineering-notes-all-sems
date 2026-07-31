### RSA public key cryptography

- RSA is a type of public-key cryptography that is widely used for secure data transmission over the internet  .
- Public-key cryptography involves a pair of keys known as a public key and a private key, which are associated with an entity that needs to authenticate its identity electronically or to sign or encrypt data.
- The public key is made available to anyone who needs it, while the private key is kept secret by the owner.
- RSA is named after its inventors, Ronald L. Rivest, Adi Shamir, and Leonard M. Adleman, who publicly described the algorithm in 1977 .
- The basic idea of RSA is to use the mathematical properties of large prime numbers and modular arithmetic to create a one-way function that is easy to compute in one direction, but hard to invert in the other direction.
- The one-way function used by RSA is based on the difficulty of factoring the product of two large prime numbers, which is known as the RSA problem .
- The RSA algorithm consists of the following steps:
  - Key generation: The sender and the receiver each choose two large prime numbers, p and q, and compute their product, n = pq, which is called the modulus. They also choose a public exponent, e, that is coprime with (p-1)(q-1), and compute the private exponent, d, such that ed ≡ 1 (mod (p-1)(q-1)). The public key is (n, e) and the private key is (n, d).
  - Encryption: To encrypt a message, m, the sender computes the ciphertext, c, as c = m^e (mod n), and sends it to the receiver.
  - Decryption: To decrypt the ciphertext, c, the receiver computes the plaintext, m, as m = c^d (mod n), using the private key.
- RSA is secure as long as the factorization of n is hard, which means that p and q should be large enough and chosen randomly .
- RSA can be used for both encryption and digital signatures, as well as for key exchange and authentication  .
- RSA is commonly used in the establishment of SSL/TLS sessions, and by the OpenVPN protocol and sometimes IKEv2 to secure the TLS handshake.