### Random Number Generation

Random number generation is a very important topic in Cryptography. It is the technique that helps us avoid brute force attacks. A brute force attack is when the attacker tries all possible keys to try to decode an encrypted message.

- Cryptographic applications typically make use of algorithmic techniques for random number generation. These algorithms are deterministic and therefore produce sequences of numbers that are not statistically random. However, if the algorithm is good, the resulting sequences will pass many reasonable tests of randomness.

- A popular approach to generating secure pseudorandom number is known as the Blum, Blum, Shub (BBS) generator, named for its developers [BLUM86]. It has perhaps the strongest public proof of its cryptographic strength. The procedure is as follows. First, choose two large prime numbers, p and q, that both have a remainder of 3 when divided by 4.

- The generation of random numbers is essential to cryptography. One of the most difficult aspect of cryptographic algorithms is in depending on or generating, true random information. This is problematic, since there is no known way to produce true random data, and most especially no way to do so on a finite state machine such as a computer.

- Approved Random Number Generators for FIPS PUB 140-2, Security Requirements for Cryptographic Modules are available from the National Institute of Standards and Technology (NIST).

- Algorithm specifications for current FIPS-approved and NIST-recommended random number generators are available from the Cryptographic Toolkit. Current testing includes the following algorithm: DRBG (SP 800-90A).
