### RSA public key cryptography

- RSA is a type of public-key cryptography that is widely used for secure data transmission over the internet  .
- Public-key cryptography involves a pair of keys known as a public key and a private key, which are associated with an entity that needs to authenticate its identity electronically or to sign or encrypt data.
- The public key is made available to anyone who needs it, while the private key is kept secret by the owner.
- RSA is named after its inventors, Ronald L. Rivest, Adi Shamir, and Leonard M. Adleman, who publicly described the algorithm in 1977 .
- The RSA algorithm works as follows:
  - Choose two large prime numbers p and q, and compute their product n = pq, which is called the modulus.
  - Choose a small number e, which is relatively prime to (p-1)(q-1), and is called the public exponent.
  - Compute a number d, which is the multiplicative inverse of e modulo (p-1)(q-1), and is called the private exponent.
  - The public key consists of (n, e), and the private key consists of (n, d).
  - To encrypt a message m, compute c = m^e mod n, and send c to the receiver.
  - To decrypt a ciphertext c, compute m = c^d mod n, and recover the original message m.
- The security of RSA relies on the difficulty of factoring large numbers, which is a hard problem in computational number theory.
- RSA is most commonly used in the establishment of an SSL/TLS session, and by the OpenVPN protocol and sometimes IKEv2 to secure the TLS handshake.
- RSA can also be used for digital signatures, which allow the sender to prove the authenticity and integrity of a message.
- RSA has some limitations, such as being slower than symmetric-key algorithms, and being vulnerable to chosen ciphertext attacks if not implemented properly.