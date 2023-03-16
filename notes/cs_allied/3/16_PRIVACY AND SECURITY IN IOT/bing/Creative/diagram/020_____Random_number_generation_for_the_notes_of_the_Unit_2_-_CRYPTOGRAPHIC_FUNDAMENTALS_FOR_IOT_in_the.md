Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Privacy and Security in IoT. Here is the content for the topic of Random number generation for the notes of the Unit 2 - Cryptographic Fundamentals for IoT.

### Random number generation

- Random numbers are essential for cryptography, as they are used for generating keys, initialization vectors, nonces, challenges, and other parameters.
- A random number generator (RNG) is a device or algorithm that produces a sequence of numbers that are unpredictable and have no discernible pattern or correlation.
- There are two main types of RNGs: true random number generators (TRNGs) and pseudo-random number generators (PRNGs).
- A TRNG is a physical device that relies on a source of randomness that is inherent in nature, such as thermal noise, radioactive decay, or quantum phenomena. A TRNG produces numbers that are statistically independent and uniformly distributed.
- A PRNG is a mathematical algorithm that takes an initial value, called a seed, and produces a sequence of numbers that appear random, but are actually deterministic and reproducible. A PRNG produces numbers that are statistically dependent and may have some bias or correlation.
- The quality of a RNG depends on its entropy, which is a measure of the unpredictability or randomness of its output. The higher the entropy, the more secure the RNG is.
- A TRNG has high entropy, as its output is influenced by unpredictable physical processes. However, a TRNG may be slow, expensive, or difficult to implement in some devices or environments.
- A PRNG has low entropy, as its output is determined by its seed and algorithm. However, a PRNG can be fast, cheap, and easy to implement in software or hardware.
- A common approach to combine the advantages of both types of RNGs is to use a hybrid RNG, which consists of a TRNG that provides a seed to a PRNG that generates the output. This way, the output has high entropy and high speed.
- Another approach is to use a cryptographically secure PRNG (CSPRNG), which is a PRNG that satisfies two properties: unpredictability and forward security. Unpredictability means that it is computationally infeasible to predict the next output given the previous outputs. Forward security means that it is computationally infeasible to recover the previous outputs given the current output or the seed.
- A CSPRNG can be constructed from a cryptographic hash function, a block cipher, or a stream cipher, by applying them to a seed or a state that is updated periodically. Examples of CSPRNGs are the Blum-Blum-Shub algorithm, the Yarrow algorithm, and the Fortuna algorithm.
- The choice of a RNG depends on the application and the security requirements. For example, a TRNG may be suitable for generating long-term keys, while a PRNG or a CSPRNG may be suitable for generating session keys or other short-term parameters.