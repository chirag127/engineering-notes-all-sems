### Random number generation

- Random number generation is a process by which a sequence of numbers or symbols that cannot be reasonably predicted better than by random chance is generated.
- Random numbers are useful for many applications, such as cryptography, simulation, gaming, statistical sampling, and scientific experiments.
- There are two main types of random number generators: hardware-based and pseudo-random.
- Hardware-based random number generators use physical devices or phenomena, such as dice, coins, radioactive decay, or thermal noise, to produce random outcomes .
- Pseudo-random number generators use mathematical algorithms or functions, such as linear congruential generators, Mersenne Twister, or Blum Blum Shub, to produce sequences of numbers that appear random but are actually deterministic and reproducible .
- Pseudo-random number generators have advantages over hardware-based ones, such as speed, portability, and scalability, but they also have limitations, such as periodicity, correlation, and predictability.
- Pseudo-random number generators require a seed value, which is an initial input that determines the sequence of numbers generated. The seed value can be chosen randomly, such as from the current time or a hardware source, or fixed, such as a user-defined constant or a hard-coded value.
- The quality of a pseudo-random number generator can be measured by various statistical tests, such as frequency test, runs test, autocorrelation test, or chi-square test, that check how well the generated numbers match the expected properties of a true random sequence.
- Some examples of pseudo-random number generators are:

  - Linear congruential generator (LCG): a simple and widely used algorithm that generates numbers by the recurrence relation `Xn+1 = (aXn + c) mod m`, where `a`, `c`, and `m` are constants and `X0` is the seed value.
  - Mersenne Twister (MT): a more complex and popular algorithm that generates numbers by using a large state vector and a series of bitwise operations and shifts. It has a very long period of 2^19937 - 1 and passes many statistical tests.
  - Blum Blum Shub (BBS): a cryptographically secure algorithm that generates numbers by the recurrence relation `Xn+1 = Xn^2 mod N`, where `N` is the product of two large prime numbers and `X0` is the seed value. It is based on the hardness of factoring large numbers and has a high security level.

: Random number generation - Wikipedia
: Random Number Generator - Calculator