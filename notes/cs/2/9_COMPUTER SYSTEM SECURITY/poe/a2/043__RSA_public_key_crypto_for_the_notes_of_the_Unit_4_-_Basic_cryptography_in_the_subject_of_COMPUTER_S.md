 Here is the content in markdown format without any emojis or external links and in a formal tone:

### RSA public key crypto

1. RSA is an asymmetric key algorithm - it uses a public key and a private key. The public key can be shared with everyone while the private key is kept secret.
2. To generate the keys, two large prime numbers (p and q) are chosen. Their product n = p * q is computed.
3. A number e is chosen such that 1 < e < (p-1) * (q-1) and e is co-prime to (p-1) * (q-1). e is the public key.
4. A number d is calculated such that (e * d) % ((p-1) * (q-1)) = 1. d is the private key.
5. To encrypt a message M, calculate C = M^e mod n. To decrypt, calculate M = C^d mod n.
6. The strength of RSA lies in the difficulty of factoring very large numbers. As long as p and q remain secret, it is not feasible to deduce the private key from the public key.
7. RSA is commonly used to encrypt session keys for symmetric key encryption and to create digital signatures. It is secure if large enough key sizes are used.

The content summarizes the key points around how RSA public key cryptography works. The points are written in a formal tone with no emojis or external links as requested. Please let me know if you would like me to modify or expand the content in any way.