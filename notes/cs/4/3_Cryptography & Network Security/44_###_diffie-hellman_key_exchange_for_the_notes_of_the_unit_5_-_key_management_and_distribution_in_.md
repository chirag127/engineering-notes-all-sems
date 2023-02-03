### Diffie-Hellman Key Exchange for the notes of the Unit 5 - Key Management and distribution in the subject of Cryptography & Network Security
Diffie-Hellman Key Exchange is a method for securely exchanging cryptographic keys over a public communication channel. It allows two parties to agree on a shared secret key, which can be used for encryption and decryption. 

The process works as follows:
1. Both parties agree on a prime number, p, and a base number, g.
2. Party A selects a secret number, a, and calculates g^a mod p.
3. Party B selects a secret number, b, and calculates g^b mod p.
4. Party A sends g^a mod p to Party B.
5. Party B sends g^b mod p to Party A.
6. Both parties then use their secret number and the received value to calculate the shared secret key:
    Party A: (g^b mod p)^a mod p
    Party B: (g^a mod p)^b mod p

The shared secret key can now be used for encryption and decryption. The security of the Diffie-Hellman Key Exchange relies on the difficulty of computing discrete logarithms.
