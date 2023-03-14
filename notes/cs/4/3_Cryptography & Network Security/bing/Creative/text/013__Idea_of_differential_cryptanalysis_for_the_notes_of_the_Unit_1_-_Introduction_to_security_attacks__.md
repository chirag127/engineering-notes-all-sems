### Idea of differential cryptanalysis

- Differential cryptanalysis is a general form of cryptanalysis applicable primarily to block ciphers, but also to stream ciphers and cryptographic hash functions. 
- It is the study of how differences in information input can affect the resultant difference at the output. 
- It is usually a chosen plaintext attack, meaning that the attacker must be able to obtain ciphertexts for some set of plaintexts of their choosing. 
- The basic method uses pairs of plaintext related by a constant difference, and traces how the difference propagates through the cipher. 
- The attacker exploits the non-random behavior of the cipher to recover the secret key. 
- Differential cryptanalysis was first publicized in 1990 by Biham and Shamir, who showed attacks against reduced-round variants of DES and other ciphers. 
- It was later revealed that differential cryptanalysis was known to IBM and NSA as early as 1974, and that DES was designed with resistance to it in mind.  
- Differential cryptanalysis can be applied to various block cipher structures, such as Feistel networks, substitution-permutation networks, and SPONGENT. 
- It can also be extended to other modes of attack, such as known plaintext, ciphertext-only, or related-key. 
- It can also be combined with other techniques, such as linear cryptanalysis, boomerang attack, or impossible differential cryptanalysis. 

: Differential cryptanalysis - Wikipedia
: Differential Cryptanalysis | SpringerLink