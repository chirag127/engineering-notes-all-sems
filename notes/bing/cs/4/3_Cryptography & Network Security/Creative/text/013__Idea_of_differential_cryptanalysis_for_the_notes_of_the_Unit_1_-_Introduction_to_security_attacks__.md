### Idea of differential cryptanalysis

- Differential cryptanalysis is a general form of cryptanalysis applicable primarily to block ciphers, but also to stream ciphers and cryptographic hash functions.
- It is the study of how differences in information input can affect the resultant difference at the output.
- It is usually a chosen plaintext attack, meaning that the attacker must be able to obtain ciphertexts for some set of plaintexts of their choosing.
- The basic method uses pairs of plaintext related by a constant difference, and looks at the differences in the resulting ciphertext pairs.
- Based on these differences, probabilities are assigned to possible keys.
- As more pairs are analyzed, the probability concentrates around a smaller number of keys.
- The attacker can then use other techniques to find the most likely key among the candidates.
- Differential cryptanalysis was first publicized in 1990 by Biham and Shamir with attacks against reduced-round variants of DES.
- It was followed in 1991 by the first attack against DES which was faster than exhaustive search.
- Differential cryptanalysis can also be used to find weaknesses in the design of block ciphers and hash functions, and to evaluate their resistance to this type of attack.