### Idea of Differential Cryptanalysis

Differential Cryptanalysis is a powerful technique used to analyze and break symmetric key cryptographic systems. It was first introduced by Biham and Shamir in 1991 and has since become one of the most important cryptanalysis techniques.

Differential cryptanalysis works by analyzing the differences between pairs of plaintexts and the corresponding ciphertexts. By analyzing these differences, the attacker can derive information about the key used in the encryption process.

In order to perform differential cryptanalysis, the attacker needs pairs of plaintexts and the corresponding ciphertexts that differ in only a few bits. The attacker then calculates the difference between the plaintexts and the corresponding ciphertexts and uses this information to derive the key.

The basic idea behind differential cryptanalysis is to find a differential characteristic that holds with a high probability for a given cipher. This characteristic is then used to derive information about the key.

Differential cryptanalysis can be used to attack both block ciphers and stream ciphers. However, it is particularly effective against block ciphers because they operate on fixed size blocks of data.

In order to protect against differential cryptanalysis, designers of cryptographic systems need to carefully choose the S-boxes and the P-boxes used in the encryption process. They also need to ensure that the round functions of the cipher are designed to provide good diffusion and confusion.

Overall, differential cryptanalysis is a powerful technique that can be used to break many symmetric key cryptographic systems. Designers of cryptographic systems need to be aware of this technique and take steps to protect against it.