### Idea of differential cryptanalysis for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

- Differential cryptanalysis is a general form of cryptanalysis applicable primarily to block ciphers, but also to stream ciphers and cryptographic hash functions. 
- It is the study of how differences in information input can affect the resultant difference at the output. 
- It is usually a chosen plaintext attack, meaning that the attacker must be able to obtain ciphertexts for some set of plaintexts of their choosing. 
- The basic method uses pairs of plaintext related by a constant difference, usually XOR. 
- The attacker then analyzes the differences in the corresponding ciphertext pairs, and assigns probabilities to possible keys based on the observed patterns. 
- The attack exploits the fact that some differences in the input may cause certain differences in the output with a probability higher or lower than the expected 50%. 
- This indicates a non-random behavior of the cipher, and reveals some information about the key. 
- The attack can be applied to ciphers based on substitutions and permutations, such as DES and FEAL. 
- The attack is more efficient than brute force, but it requires a large number of chosen plaintexts and a complex statistical analysis. 
- The attack was discovered by Eli Biham and Adi Shamir in the late 1980s, but it was also known to IBM and NSA in the 1970s. 
- DES was designed with resistance to differential cryptanalysis in mind, but small modifications to the algorithm would make it much more susceptible. 

: Differential cryptanalysis - Wikipedia
: Differential Cryptanalysis - an overview | ScienceDirect Topics